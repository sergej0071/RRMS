from apscheduler.schedulers.background import BackgroundScheduler
from rrms_web_app.models import MainData
from django.utils import timezone
from rrms_arduino_app.arduinoService import ArduinoService
from rrms_project.settings import IS_MOCK_SCHEDULER
import random

def take_perception_data(_arduinoService):
    if(IS_MOCK_SCHEDULER):
        e = MainData.objects.create(
            temperature=random.randint(10, 30),
            pressure=random.randint(30, 70),
            humidity=random.randint(100, 1500),
            timeData=str(timezone.now()))
        
    else:
        data = _arduinoService.getArduinoModel()
        if(data != None):
            e = MainData.objects.create(
                temperature=data[2].replace("\r\n", ""),
                pressure=data[1],
                humidity=data[0],
                timeData=str(timezone.now()))
        


def start():
    _arduinoService = ArduinoService()
    scheduler = BackgroundScheduler()
    scheduler.add_job(take_perception_data, 'interval', seconds=2.0, name='do-some', jobstore='default', args=[_arduinoService])
    scheduler.start()