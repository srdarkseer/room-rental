
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProvinceViewSet, DistrictViewSet, LocalLevelViewSet, LocalAreaViewSet

router = DefaultRouter()
router.register(r'provinces', ProvinceViewSet)
router.register(r'districts', DistrictViewSet)
router.register(r'local-levels', LocalLevelViewSet)
router.register(r'local-areas', LocalAreaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

