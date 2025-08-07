from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import IoTEvent
from .serializers import IoTEventSerializer

class IoTEventViewSet(viewsets.ModelViewSet):
    queryset = IoTEvent.objects.all()
    serializer_class = IoTEventSerializer
    permission_classes = [IsAuthenticated]  # <- ISSO exige token JWT