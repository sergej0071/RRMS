from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events
from smrr_rest_app.models import MainData
from django.utils import timezone
from scheduler.arduinoTicknessService import ArduinoTicknessService

def take_perception_data(_arduinoService):
    data = _arduinoService.getArduinoModel()
    
    if(data != None):
        e = MainData.objects.create(temperature=data[2].replace("\r\n", ""), pressure=data[1], humidity=data[0], timeadata=str(timezone.now()))

def start():
    _arduinoService = ArduinoTicknessService()
    scheduler = BackgroundScheduler()
    scheduler.add_job(take_perception_data, 'interval', seconds=2.0, name='do-some', jobstore='default', args=[_arduinoService])
    scheduler.start()