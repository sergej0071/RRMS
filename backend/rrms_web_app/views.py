from rest_framework.views import APIView
from django.http import JsonResponse
from django.http import HttpResponse
from .models import MainData
import logging

logger = logging.getLogger('error_logger')

class CurrentStatus(APIView):
    def get(self,request):
        try:
            j = MainData.objects.last()
            j_dict = {"temperature":j.temperature, "pressure":j.pressure, "humidity":j.humidity}
        except Exception as e:
            logger.error(f'An exception occurred in ArduinoTicknessService. exeption - {e} ')
            return HttpResponse(status=400)
        return JsonResponse(j_dict, safe=False)

class LastValues(APIView):
    def get(self,request):
        response = {}
        try:
            amount = request.headers.get('amount')
            query = MainData.objects.all()
            try:
                j = query.values('temperature', 'pressure', 'humidity', 'timeadata')[:int(amount)]
            except:
                j = query.values('temperature', 'pressure', 'humidity','timeadata')            
            response = list(j)
        except Exception as e:
            logger.error(f'An exception occurred in ArduinoTicknessService. exeption - {e} ')
            return HttpResponse(status=400)
        return JsonResponse(response, safe=False)