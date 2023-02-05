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
from rrms_web_app.viewHelpers.genericORMaRepository import GenericORMaRepository
from rrms_scheduler_app.services.dataExplorationService import DataExplorationService
from rrms_scheduler_app.services.predictionService import PredictionService
from rrms_web_app.viewHelpers.dataMapperHelper import DataMapperHelper
from varname import nameof
import logging

class CurrentStatus(APIView):
    def __init__(self):
            self.logger = logging.getLogger('error_logger')
            self._genericORMRepository = GenericORMaRepository()
    
    def get(self,request):
        response = {}
        try:
            response = self._genericORMRepository.getLastElement(MainData, 'temperature', 'pressure', 'humidity')

            if(response is None):
                return HttpResponse(status=500)
            return JsonResponse(response, safe=False)
        
        except Exception as e:
            self.logger.error(f'An exception occurred in {nameof(CurrentStatus)}. exeption - {e} ')
            return HttpResponse(status=500)
        
        return JsonResponse(response, safe=False)

class LastValues(APIView):
    def __init__(self):
        self._dataMapperHelper = DataMapperHelper()
        self._genericORMRepository = GenericORMaRepository()
        self._predictService = PredictionService()
        self.logger = logging.getLogger('error_logger')
    
    def get(self, request, amount=5):
        response = {}
        try:
            response = self._returnRealAndPredictData(self._genericORMRepository
                    .getLastElements(MainData, amount, 'temperature', 'pressure', 'humidity', 'timeData'))
            
            if(response is None):
                return HttpResponse(status=500)
            return JsonResponse(response, safe=False)

        except Exception as e:
            self.logger.error(f'An exception occurred in {nameof(LastValues)}. exeption - {e} ')
            return HttpResponse(status=500)
        return JsonResponse(response, safe=False)
    
    def _returnRealAndPredictData(self, realData):
        timePeriod = 1
        data = self._predictService.modifyPredictedTime(self._dataMapperHelper.splitArrayBykey(realData, 'timeData'), timePeriod)

        temperatureArray = self._predictService.getPredictionValue(self._dataMapperHelper.splitArrayBykey(realData,'temperature'), timePeriod)
        pressureArray = self._predictService.getPredictionValue(self._dataMapperHelper.splitArrayBykey(realData, 'pressure'), timePeriod)
        humidityArray = self._predictService.getPredictionValue(self._dataMapperHelper.splitArrayBykey(realData, 'humidity'), timePeriod)

        predictData = []
        for i in range(len(data)):            
            predictData.append(
                {
                    'temperature' : temperatureArray[i],
                    'pressure' : pressureArray[i],
                    'humidity' : humidityArray[i],
                    'timeData' : data[i]
                })

        return {
                'realData': realData,
                'prognosisData': predictData
                }


class Correlation(APIView):
    def __init__(self):
        self._dataMapperHelper = DataMapperHelper()
        self._genericORMRepository = GenericORMaRepository()
        self._dataExplorationService = DataExplorationService()
        self.logger = logging.getLogger('error_logger')
        
    def get(self, request, amount=5):
        try:
            data = self._genericORMRepository.getLastElements(MainData, amount, 'temperature', 'pressure', 'humidity')

            if(data is None):
                return HttpResponse(status=500)
            
            temperatureArray = self._dataMapperHelper.splitArrayBykey(data,'temperature')
            pressureArray = self._dataMapperHelper.splitArrayBykey(data, 'pressure')
            humidityArray = self._dataMapperHelper.splitArrayBykey(data, 'humidity')

            temperaturePressureCorr = self._dataExplorationService.getCorrelationCoefficient(temperatureArray, pressureArray)
            temperatureHumidityCorr = self._dataExplorationService.getCorrelationCoefficient(temperatureArray, humidityArray)
            pressureHumidityCorr = self._dataExplorationService.getCorrelationCoefficient(pressureArray, humidityArray)

            respons = {
                    'data': 
                        { 
                            'temperature': temperatureArray,
                            'humidity': pressureArray,
                            'pressure': humidityArray
                        },
                    'coefCorrelation': 
                        {
                            'temperaturePressure': temperaturePressureCorr,
                            'temperatureHumidity': temperatureHumidityCorr,
                            'pressureHumidity': pressureHumidityCorr                        
                        }
                    } 
            
            return JsonResponse(respons, safe=False)

        except Exception as e:
            self.logger.error(f'An exception occurred in {nameof(Correlation)}. exeption - {e} ')
            return HttpResponse(status=500)
        return JsonResponse(response, safe=False)


class ProbabilityDiagram(APIView):
    def __init__(self):
        self._dataMapperHelper = DataMapperHelper()
        self._genericORMRepository = GenericORMaRepository()
        self._dataExplorationService = DataExplorationService()
        self.logger = logging.getLogger('error_logger')
        
    def get(self, request, amount=5):
        try:
            data = self._genericORMRepository.getLastElements(MainData, amount, 'temperature', 'pressure', 'humidity')

            if(data is None):
                return HttpResponse(status=500)

            temperatureArrayV, temperatureArrayA = self._dataExplorationService.getUniqueValuesAndAmount(self._dataMapperHelper.splitArrayBykey(data,'temperature'))
            pressureArrayV, pressureArrayA = self._dataExplorationService.getUniqueValuesAndAmount(self._dataMapperHelper.splitArrayBykey(data, 'pressure'))
            humidityArrayV, humidityArrayA = self._dataExplorationService.getUniqueValuesAndAmount(self._dataMapperHelper.splitArrayBykey(data, 'humidity'))

            response =  {
                    'temperature':
                     {
                        "value":  temperatureArrayV,
                        "amount": temperatureArrayA
                     },
                    'pressure': 
                     {
                        "value":  pressureArrayV,
                        "amount": pressureArrayA
                     },
                    'humidity': 
                     {
                        "value":  humidityArrayV,
                        "amount": humidityArrayA
                     },
                    }

            return JsonResponse(response, safe=False)

        except Exception as e:
            self.logger.error(f'An exception occurred in {nameof(ProbabilityDiagram)}. exeption - {e} ')
            return HttpResponse(status=500)
        return JsonResponse({}, safe=False)