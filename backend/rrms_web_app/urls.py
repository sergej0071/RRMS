from django.urls import path, include, re_path
from . import views

app_name = 'rest_endpoins'

urlpatterns = [
    path('current/', views.CurrentStatus.as_view()),
    path('last_values/', views.LastValues.as_view()),

]