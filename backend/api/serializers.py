# api/serializers.py
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models import Country, Region, Year, CountryRegion, EconomicData, SocialSupportData, HealthData

class WorldHappinessTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # カスタムのクレームを追加
        token['username'] = user.username
        token['email'] = user.email

        return token

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

class CountrySerializer(serializers.ModelSerializer):
    region_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Region.objects.all(),
        source='region'
    )

    class Meta:
        model = Country
        fields = ['id', 'name', 'region_id']

    def create(self, validated_data):
        # validated_data から region を取得
        region = validated_data.pop('region', None)
        country = Country.objects.create(**validated_data)
        
        if region:
            # 選択されたリージョンを使って CountryRegion インスタンスを作成
            CountryRegion.objects.create(country=country, region=region)
        
        return country

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'name']  # 必要に応じてフィールドを調整

class YearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Year
        fields = ['id', 'year']  # IDフィールドを追加

class CountryRegionSerializer(serializers.ModelSerializer):
    country_id = serializers.PrimaryKeyRelatedField(
        source='country',
        queryset=Country.objects.all(),
        write_only=True
    )
    region_id = serializers.PrimaryKeyRelatedField(
        source='region',
        queryset=Region.objects.all(),
        write_only=True
    )
    country = serializers.StringRelatedField(read_only=True)  # 読み取り専用
    region = serializers.StringRelatedField(read_only=True)   # 読み取り専用

    # 追加する部分
    id = serializers.IntegerField(source='pk', read_only=True)

    class Meta:
        model = CountryRegion
        fields = ['id', 'country_id', 'region_id', 'country', 'region']

class EconomicDataSerializer(serializers.ModelSerializer):
    country_region = CountryRegionSerializer(read_only=True)
    year = YearSerializer(read_only=True)
    # POSTリクエストでcountry_regionをIDで受け取るために以下のフィールドを追加
    country_region_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=CountryRegion.objects.all(),
        source='country_region'
    )
    year_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Year.objects.all(),
        source='year'
    )

    class Meta:
        model = EconomicData
        fields = '__all__'  # 必要に応じてフィールドを調整
        extra_kwargs = {
            'country_region': {'read_only': True},
            'year': {'read_only': True}
        }

class SocialSupportDataSerializer(serializers.ModelSerializer):
    country_region = CountryRegionSerializer(read_only=True)
    year = YearSerializer(read_only=True)

    country_region_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=CountryRegion.objects.all(),
        source='country_region'
    )
    year_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Year.objects.all(),
        source='year'
    )

    class Meta:
        model = SocialSupportData
        fields = '__all__' 
        extra_kwargs = {
            'country_region': {'read_only': True},
            'year': {'read_only': True}
        }

class HealthDataSerializer(serializers.ModelSerializer):
    country_region = CountryRegionSerializer(read_only=True)
    year = YearSerializer(read_only=True)

    country_region_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=CountryRegion.objects.all(),
        source='country_region'
    )
    year_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Year.objects.all(),
        source='year'
    )

    class Meta:
        model = HealthData
        fields = '__all__' 
        extra_kwargs = {
            'country_region': {'read_only': True},
            'year': {'read_only': True}
        }
        
         