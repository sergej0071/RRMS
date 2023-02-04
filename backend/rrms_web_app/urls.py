from django.urls import path, include, re_path
from . import views

app_name = 'rrms_web_app'

urlpatterns = [
    path('current/', views.CurrentStatus.as_view()),
    path('last_values/', views.LastValues.as_view()),

]