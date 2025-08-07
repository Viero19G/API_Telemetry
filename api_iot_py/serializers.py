from rest_framework import serializers
from .models import IoTEvent
from datetime import datetime

class IoTEventSerializer(serializers.ModelSerializer):
    # Campo extra para receber o timestamp como UNIX (segundos)
    timestamp_unix = serializers.IntegerField(write_only=True)

    class Meta:
        model = IoTEvent
        fields = ['id', 'device_id', 'state', 'timestamp','hours_powered', 'hours_worked', 'timestamp_unix']
        read_only_fields = ['timestamp']  # timestamp calculado, não editável diretamente

    def create(self, validated_data):
        # Extrai e converte timestamp_unix em datetime
        timestamp_unix = validated_data.pop('timestamp_unix')
        validated_data['timestamp'] = datetime.fromtimestamp(timestamp_unix)
        return super().create(validated_data)