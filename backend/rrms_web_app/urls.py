from django.urls import path
from . import views

app_name = 'rrms_web_app'

urlpatterns = [
    path('current/', views.CurrentStatus.as_view(), name="current"),
    path('last-values/<int:amount>', views.LastValues.as_view()),
    path('probability/<int:amount>', views.ProbabilityDiagram.as_view()),
    path('correlation/<int:amount>', views.Correlation.as_view())
]