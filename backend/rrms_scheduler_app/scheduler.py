from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events
from smrr_rest_app.models import MainData
from django.utils import timezone
from scheduler.arduinoTicknessService import ArduinoTicknessService



def start():
    _arduinoService = ArduinoTicknessService()
    scheduler = BackgroundScheduler()
    scheduler.add_job(take_perception_data, 'interval', seconds=2.0, name='do-some', jobstore='default', args=[_arduinoService])
    scheduler.start()