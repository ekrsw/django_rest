from django.urls import path, include
from rest_framework import routers

from .views import UserViewSet, UserCreateAPIView

router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create/', UserCreateAPIView.as_view(), name='create'),
]