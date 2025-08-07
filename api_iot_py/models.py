from django.db import models

"""
Classe estruturada e pensada para receber o JSON
{
  "id":  "robustec0001", 
  "state": "stop",
  "timestamp": 1754510232, 
  "hours_powered":  1234.56,
  "hours_worked":  1234.56
}

Sendo que "state" pode receber:
- off - máquina sem energia
- stopped - máquina com energia e não operando
- running - máquina com energia e operando
- turned on (evento) - máquina começou a receber energia
- turned off (evento) - máquina deixou de receber energia
- start (evento) - máquina começou a operar
- stop (evento) - máquina deixou de operar
"""

class IoTEvent(models.Model):
    DEVICE_STATE_CHOICES = [
        ('off', 'off'),
        ('stopped', 'stopped'),
        ('running', 'running'),
        ('turned_on', 'turned_on'),
        ('turned_off', 'turned_off'),
        ('start', 'start'),
        ('stop', 'stop'),
    ]

    device_id = models.CharField(max_length=100)  # vem do campo "id" no JSON
    state = models.CharField(max_length=10, choices=DEVICE_STATE_CHOICES)
    timestamp = models.DateTimeField()  # será convertido antes de salvar
    hours_powered = models.FloatField()
    hours_worked = models.FloatField()

    def __str__(self):
        return f"{self.device_id} - {self.state} @ {self.timestamp}"
