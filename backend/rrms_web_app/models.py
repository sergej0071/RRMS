
from djongo import models
# Create your models here.

class MainData(models.Model):
    _id = models.ObjectIdField()
    temperature = models.FloatField()
    pressure = models.FloatField()
    humidity = models.FloatField()
    timeadata = models.DateTimeField()
