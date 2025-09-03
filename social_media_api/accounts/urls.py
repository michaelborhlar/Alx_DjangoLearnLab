from django.urls import path
from rest_framework import DefaultRouter
from .views import CustomUserViewSet


router = DefaultRouter
router.register(r"CustomUser", CustomUserViewSet)

urlpatterns = [
    path('', include("account.urls"))
]
