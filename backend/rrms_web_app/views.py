from rest_framework.views import APIView
from django.http import JsonResponse

class CurrentStatus(APIView):
    def get(self,request):        
        return JsonResponse({})

class LastValues(APIView):
    def get(self, request):
        return JsonResponse({})