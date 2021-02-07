from django.db import models
from measurements.models import Measurement

# Create your models here.
class Alarm(models.Model):
    measurements = models.ManyToManyField(Measurement)
    
    def __str__(self):
        return '{}'.format(self.measurements)