# api_iot_py/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IoTEventViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'iot-events', IoTEventViewSet, basename='iot-event')

urlpatterns = [
    # JWT Auth
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # CRUD endpoints
    path('', include(router.urls)),
]
