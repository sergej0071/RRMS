
from django.db import models
# Create your models here.

class MainData(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    temperature = models.FloatField()
    pressure = models.FloatField()
    humidity = models.FloatField()
    timeadata = models.DateTimeField()