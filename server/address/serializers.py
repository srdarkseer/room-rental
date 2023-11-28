from rest_framework import serializers
from .models import Province, District, LocalLevel, LocalArea


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = '__all__'


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'


class LocalLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalLevel
        fields = '__all__'


class LocalAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalArea
        fields = '__all__'

