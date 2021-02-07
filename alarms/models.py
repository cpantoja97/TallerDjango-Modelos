from django.db import models
from measurements.models import Measurement

# Create your models here.
class Alarm(models.Model):
    measurements = models.ManyToManyField(Measurement)
    name = models.CharField(max_length=50)
    def __str__(self):
        return '{}'.format(self.name)    
        