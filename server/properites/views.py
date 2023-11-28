# views.py

from rest_framework import viewsets, permissions
from .models import Property, PropertyImage, PropertyPrice, PropertyLocation, PropertyStatus, PropertyType
from .serializers import  PropertySerializer, PropertyImageSerializer, PropertyPriceSerializer, PropertyLocationSerializer, PropertyStatusSerializer,PropertyTypeSerializer
from utils.permissions import IsAdminOrReadOnly, IsAuthenticatedOwnerOrReadOnly


class PropertyTypeViewSet(viewsets.ModelViewSet):
    queryset = PropertyType.objects.all()
    serializer_class = PropertyTypeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsAdminOrReadOnly]
    
    

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthenticatedOwnerOrReadOnly]
    
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

class PropertyStatusViewSet(viewsets.ModelViewSet):
    queryset = PropertyStatus.objects.all()
    serializer_class = PropertyStatusSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthenticatedOwnerOrReadOnly]