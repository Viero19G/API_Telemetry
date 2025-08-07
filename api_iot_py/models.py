from django.db import models

"""Classe estruturada e pensada para receber o JSON
{
  "id":  "robustec0001", 
  "state": "stop",
  "timestamp": 1754510232, 
  "hours_worked":  1234.56
}

Sendo que "state" pode receber:
- start
- stop
- running
- stopped"""

class IoTEvent(models.Model):
    DEVICE_STATE_CHOICES = [
        ('start', 'Start'),
        ('stop', 'Stop'),
        ('running', 'Running'),
        ('stopped', 'Stopped'),
    ]

    device_id = models.CharField(max_length=100)  # vem do campo "id" no JSON
    state = models.CharField(max_length=10, choices=DEVICE_STATE_CHOICES)
    timestamp = models.DateTimeField()  # será convertido antes de salvar
    hours_worked = models.FloatField()

    def __str__(self):
        return f"{self.device_id} - {self.state} @ {self.timestamp}"
