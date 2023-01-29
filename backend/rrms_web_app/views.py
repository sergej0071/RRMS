from rest_framework.views import APIView
from django.http import JsonResponse
from rrms_arduino_app.arduinoService import ArduinoService

class CurrentStatus(APIView):
    def get(self,request):

        x = ArduinoService()
        sad =  x.getArduinoModel()


        try:
            j = {
                    "temperature": 12.22,
                    "pressure": 34.54,
                    "humidity": 56.46                   
                }
        except Exception as e:
            return JsonResponse({"errors":str(e)})
        return JsonResponse(j)

class LastValues(APIView):
    def get(self,request):
        try:
            j = {
                    "":
                    {
                        "temperature": 12.22,
                        "pressure": 34.54,
                        "humidity": 56.46,
                        "timeadata": 1673731147363    
                    }, 
                }        
        except Exception as e:
            return JsonResponse({"errors":str(e)})
        return JsonResponse(j)