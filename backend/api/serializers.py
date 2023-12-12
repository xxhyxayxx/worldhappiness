# api/serializers.py
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models import Country, Region, Year, CountryRegion, EconomicData

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
    class Meta:
        model = Country
        fields = ['id', 'name']  # 必要に応じてフィールドを調整

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'name']  # 必要に応じてフィールドを調整

class YearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Year
        fields = ['year']

# CountryRegionSerializerは、CountryとRegionのidまたはインスタンスを受け取るように変更します
class CountryRegionSerializer(serializers.ModelSerializer):
    country = serializers.StringRelatedField()  # Country オブジェクトの文字列表現を使用
    region = serializers.StringRelatedField()  # Region オブジェクトの文字列表現を使用

    class Meta:
        model = CountryRegion
        fields = ['country', 'region']

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
        
         