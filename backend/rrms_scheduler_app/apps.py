from django.apps import AppConfig

class SchedulerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rrms_scheduler_app'

    def ready(self):      
        from rrms_scheduler_app import scheduler      
        scheduler.start()
