# urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PropertyTypeViewSet, PropertyViewSet, PropertyImageViewSet, PropertyPriceViewSet, PropertyLocationViewSet, PropertyStatusViewSet

router = DefaultRouter()

router.register(r'property-types', PropertyTypeViewSet)
router.register(r'', PropertyViewSet)
router.register(r'property-images', PropertyImageViewSet)
router.register(r'property-prices', PropertyPriceViewSet)
router.register(r'property-locations', PropertyLocationViewSet)
router.register(r'property-statuses', PropertyStatusViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
