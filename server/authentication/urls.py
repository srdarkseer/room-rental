from django.urls import path
from .views import LogoutAPIView, GoogleSocialAuthView

urlpatterns = [
    path('logout/', LogoutAPIView.as_view(), name="logout"),
    path('google/', GoogleSocialAuthView.as_view()),
]
