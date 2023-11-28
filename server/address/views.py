from rest_framework import viewsets
from .models import Province, District, LocalLevel, LocalArea 
from .serializers import ProvinceSerializer, DistrictSerializer, LocalLevelSerializer, LocalAreaSerializer

# Create your views here.

class ProvinceViewSet(viewsets.ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer

class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer

class LocalLevelViewSet(viewsets.ModelViewSet):
    queryset = LocalLevel.objects.all()
    serializer_class = LocalLevelSerializer

class LocalAreaViewSet(viewsets.ModelViewSet):
    queryset = LocalArea.objects.all()
    serializer_class = LocalAreaSerializer
