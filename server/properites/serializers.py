# serializers.py

from rest_framework import serializers
from .models import  Property, PropertyImage, PropertyPrice, PropertyLocation, PropertyStatus, PropertyType


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


class PropertyStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyStatus
        fields = '__all__'


class PropertySerializer(serializers.ModelSerializer):
    property_image = PropertyImageSerializer(many=True, read_only=True)
    latest_price = serializers.SerializerMethodField()
    property_type = PropertyTypeSerializer()
    property_location = PropertyLocationSerializer()
    property_status = serializers.SerializerMethodField()

    class Meta:
        model = Property
        exclude = ('property_price',)
    

    def get_latest_price(self, obj):
        latest_price = PropertyPrice.objects.filter(property=obj).order_by('-updated_at').first()
        if latest_price:
            return PropertyPriceSerializer(latest_price).data
        return None
    
    def get_property_status(self, obj):
        property_status = PropertyStatus.objects.filter(property=obj).filter(end_date=None)
        if property_status.exists():
            return "not available"
        else:
            return "available"
 
    
    
