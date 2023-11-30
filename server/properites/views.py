# views.py

from rest_framework import viewsets, permissions
from .models import Property, PropertyImage, PropertyPrice, PropertyLocation, PropertyStatus, PropertyType
from .serializers import  PropertySerializer, PropertyImageSerializer, PropertyPriceSerializer, PropertyLocationSerializer, PropertyTypeSerializer
from utils.permissions import IsAdminOrReadOnly, IsAuthenticatedOwnerOrReadOnly
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

class PropertyTypeViewSet(viewsets.ModelViewSet):
    queryset = PropertyType.objects.all()
    serializer_class = PropertyTypeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsAdminOrReadOnly]
    
    

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthenticatedOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['property_type','no_bedrooms', 'property_price', 'property_location', 'record']
    search_fields = ['property_name', 'property_description']
    
    def perform_create(self, serializer):
        serializer.save(property_owner=self.request.user)

class PropertyImageViewSet(viewsets.ModelViewSet):
    queryset = PropertyImage.objects.all()
    serializer_class = PropertyImageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthenticatedOwnerOrReadOnly]
    

class PropertyPriceViewSet(viewsets.ModelViewSet):
    queryset = PropertyPrice.objects.all()
    serializer_class = PropertyPriceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthenticatedOwnerOrReadOnly]

class PropertyLocationViewSet(viewsets.ModelViewSet):
    queryset = PropertyLocation.objects.all()
    serializer_class = PropertyLocationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthenticatedOwnerOrReadOnly]

