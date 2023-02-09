
from django.db import models
# Create your models here.

class MainData(models.Model):
    temperature = models.FloatField()
    pressure = models.FloatField()
    humidity = models.FloatField()
    timeData = models.DateTimeField()