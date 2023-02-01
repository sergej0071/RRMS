from django.shortcuts import render
from rest_framework.views import APIView
from .models import MainData
from rest_framework.response import Response
from django.forms.models import model_to_dict
from datetime import datetime
from json import dumps
from django.http import JsonResponse
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from rrms_scheduler_app.predictionService import PredictionService
import logging

logger = logging.getLogger('error_logger')

class CurrentStatus(APIView):
    def get(self,request):
        j_dict = {}
        try:
            j = MainData.objects.last()
            j_dict = {"temperature":j.temperature, "pressure":j.pressure, "humidity":j.humidity}
        except Exception as e:
            logger.error(f'An exception occurred in CurrentStatus. exeption - {e} ')
        return JsonResponse(j_dict, safe=False)
class LastValues(APIView):
    def get(self, request, amount=5):
        response = {}
        try:
            amount = request.GET['amount']
            query = MainData.objects.all()
            try:
                j = query.values('temperature', 'pressure', 'humidity', 'timeData')[::-1][:int(amount)][::-1]
            except:
                j = query.values('temperature', 'pressure', 'humidity','timeData')
            response = self._returnRealAndPredictData(list(j))
        except Exception as e:
            logger.error(f'An exception occurred in CurrentStatus. exeption - {e} ')
            return HttpResponse(status=400)
        return JsonResponse(response, safe=False)
    
    def _returnRealAndPredictData(self, realData):
        timePeriod = 1        
        predictService = PredictionService()
        
        data = predictService.modifyPredictedTime(self._splitArrayBykey(realData, 'timeData'), timePeriod)

        temperatureArray = predictService.getPredictionValue(self._splitArrayBykey(realData,'temperature'), timePeriod)
        pressure = predictService.getPredictionValue(self._splitArrayBykey(realData, 'pressure'), timePeriod)
        humidity = predictService.getPredictionValue(self._splitArrayBykey(realData, 'humidity'), timePeriod)

        predictData = []
        for i in range(len(data)):            
            predictData.append(
                {
                    'temperature' : temperatureArray[i],
                    'pressure' : pressure[i],
                    'humidity' : humidity[i],
                    'timeData' : data[i]
                })

        return {'realData': realData,
                'prognosisData': predictData}

    def _splitArrayBykey(self, realData, key):
        value = []
        
        for i in realData:
            value.append(i[key])

        return value

