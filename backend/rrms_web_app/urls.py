from django.urls import path, include, re_path
from . import views

app_name = 'rest_endpoins'

urlpatterns = [
    path('current/', views.CurrentStatus.as_view()),
    path('last-values/<int:amount>', views.LastValues.as_view()),
    path('probability/<int:amount>', views.ProbabilityDiagram.as_view()),
    path('correlation/<int:amount>', views.Correlation.as_view())