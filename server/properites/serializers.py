# serializers.py

from rest_framework import serializers
from .models import  Property, PropertyImage, PropertyPrice, PropertyLocation, PropertyType, Record, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name','email', 'profile_pic']

class PropertyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyType
        fields = '__all__'




class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = '__all__'
        depth = 1



class PropertyPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyPrice
        fields = '__all__'


class PropertyLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyLocation
        fields = '__all__'
        depth = 1


class PropertyRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'


class PropertySerializer(serializers.ModelSerializer):
    property_image = PropertyImageSerializer(many=True, read_only=True)
    latest_price = serializers.SerializerMethodField()
    property_type = PropertyTypeSerializer()
    property_location = PropertyLocationSerializer()
    property_record = serializers.SerializerMethodField()
    property_owner = serializers.SerializerMethodField()

    class Meta:
        model = Property
        exclude = ('property_price','record')
    

    def get_latest_price(self, obj):
        latest_price = PropertyPrice.objects.filter(property=obj).order_by('-updated_at').first()
        if latest_price:
            return PropertyPriceSerializer(latest_price).data
        return None
    
    def get_property_record(self, obj):
        property_record = Record.objects.filter(property=obj).order_by('start_date').first()
        if property_record:
            return PropertyRecordSerializer(property_record).data
        return None
    
    def get_property_owner(self, obj):
        porperty_owner = User.objects.filter(email=obj.property_owner).first()
        return UserSerializer(porperty_owner).data