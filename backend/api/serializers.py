from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models import Country, Region, Year, CountryRegion, EconomicData, SocialSupportData, HealthData, HappinessScore, FreedomData, GenerosityData, GovernmentTrustData

# WorldHappinessTokenObtainPairSerializer was written with reference to the following site
# https://sushil-kamble.medium.com/django-rest-framework-react-authentication-workflow-2022-part-1-a21f22b3f358
class WorldHappinessTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        token['email'] = user.email

        return token

# RegisterSerializer was written with reference to the following site
# https://sushil-kamble.medium.com/django-rest-framework-react-authentication-workflow-2022-part-1-a21f22b3f358
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

class RegionSerializer(serializers.ModelSerializer):
    # This inner class Meta defines the serializer's behavior
    class Meta:
        model = Region  # Specifies the model that the serializer is for
        fields = ['id', 'name']  # Indicates which fields should be serialized

    # The create method is used to create a new Region instance
    # from the validated data
    def create(self, validated_data):
        return Region.objects.create(**validated_data)

    # The update method is used to update an existing Region instance
    # with the validated data
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

from rest_framework import serializers

class CountrySerializer(serializers.ModelSerializer):
    # Nested serializer to represent regions related to the country
    regions = RegionSerializer(many=True, read_only=True)
    # Field to accept region ID for write operations
    region_id = serializers.IntegerField(write_only=True, allow_null=True, required=False)

    # Custom method to add a region to a country
    def add_region_to_country(self, country, region_id):
        try:
            region = Region.objects.get(id=region_id)
            country.regions.add(region)
        except Region.DoesNotExist:
            raise serializers.ValidationError({'region_id': 'This region does not exist.'})

    # Overridden create method to handle country creation
    # and adding a region to it if provided
    def create(self, validated_data):
        region_id = validated_data.pop('region_id', None)
        country = Country.objects.create(**validated_data)

        if region_id is not None:
            self.add_region_to_country(country, region_id)

        return country

    # Overridden update method to handle country updates
    # and changing its region if provided
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()

        region_id = validated_data.get('region_id')
        if region_id is not None:
            instance.regions.clear()
            self.add_region_to_country(instance, region_id)

        return instance

    class Meta:
        model = Country
        fields = ['id', 'name', 'regions', 'region_id']


class YearSerializer(serializers.ModelSerializer):
    # Meta class defines serializer properties
    class Meta:
        model = Year
        fields = ['id', 'year']

    # Create a new Year instance
    def create(self, validated_data):
        year = Year.objects.create(**validated_data)
        return year

    # Update an existing Year instance
    def update(self, instance, validated_data):
        instance.year = validated_data.get('year', instance.year)
        instance.save()
        return instance


class CountryRegionSerializer(serializers.ModelSerializer):
    # Fields for linking country and region by ID for write operations
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
    # Read-only fields to return the country and region names
    country = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True
    )
    region = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True
    )

    class Meta:
        model = CountryRegion
        fields = ['id', 'country_id', 'region_id', 'country', 'region']


class BaseDataSerializer(serializers.ModelSerializer):
    # Nested serializers for related country-region and year data
    country_region = CountryRegionSerializer(read_only=True)
    year = YearSerializer(read_only=True)

    # Fields to accept primary keys for country-region and year for write operations
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
        abstract = True  # Marks this serializer as abstract
        
    # Overridden create method to handle creation of new instances
    def create(self, validated_data):
        return self.Meta.model.objects.create(**validated_data)

    # Overridden update method to handle updates to existing instances
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

# Economic Data
class EconomicDataSerializer(BaseDataSerializer):
    class Meta:
        model = EconomicData  # Specifies the model associated with this serializer
        fields = '__all__'  # Includes all fields from the model
        extra_kwargs = {
            'country_region': {'read_only': True},
            'year': {'read_only': True}
        }

# Social Support Data
class SocialSupportDataSerializer(BaseDataSerializer):
    class Meta:
        model = SocialSupportData
        fields = '__all__'
        extra_kwargs = {
            'country_region': {'read_only': True},
            'year': {'read_only': True}
        }

# Health Data
class HealthDataSerializer(BaseDataSerializer):
    class Meta:
        model = HealthData
        fields = '__all__'
        extra_kwargs = {
            'country_region': {'read_only': True},
            'year': {'read_only': True}
        }

# Happiness Score
class HappinessScoreSerializer(BaseDataSerializer):
    class Meta:
        model = HappinessScore
        fields = '__all__'
        extra_kwargs = {
            'country_region': {'read_only': True},
            'year': {'read_only': True}
        }

# Freedom
class FreedomDataSerializer(BaseDataSerializer):
    class Meta:
        model = FreedomData
        fields = '__all__'
        extra_kwargs = {
            'country_region': {'read_only': True},
            'year': {'read_only': True}
        }

# Generosity
class GenerosityDataSerializer(BaseDataSerializer):
    class Meta:
        model = GenerosityData
        fields = '__all__'
        extra_kwargs = {
            'country_region': {'read_only': True},
            'year': {'read_only': True}
        }

# Government Trust Data
class GovernmentTrustDataSerializer(BaseDataSerializer):
    class Meta:
        model = GovernmentTrustData
        fields = '__all__'
        extra_kwargs = {
            'country_region': {'read_only': True},
            'year': {'read_only': True}
        }
