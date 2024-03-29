from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events
from rrms_web_app.models import MainData
from django.utils import timezone
from rrms_arduino_app.arduinoService import ArduinoService
from rrms_project.settings import MOCK_SCHEDULER
import random

def take_perception_data(_arduinoService):
    data = _arduinoService.getArduinoModel()
    if(data != None):
        e = MainData.objects.create(temperature=data[2].replace("\r\n", ""), pressure=data[1], humidity=data[0], timeaData=str(timezone.now()))

    if(MOCK_SCHEDULER):
        data = _arduinoService.getArduinoModel()
        if(data != None):
            humidityR =  str(round(float(data[1])))
            temperatureR = str(round(float(data[2].replace("\r\n", "")), 2))
            MainData.objects.create(
                temperature=temperatureR,
                pressure=humidityR,
                humidity=data[0],
                timeData=str(timezone.now()))
    else:
        MainData.objects.create(
            temperature=random.randint(10, 30),
            pressure=random.randint(30, 70),
            humidity=random.randint(30, 70),
            timeData=str(timezone.now()))

def start():
    _arduinoService = ArduinoService()
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        take_perception_data,
        'interval',
        seconds=2.0,
        name='do-some',
        jobstore='default',
        args=[_arduinoService])
    scheduler.start()