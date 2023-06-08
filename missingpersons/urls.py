from django.urls import path
from missingapp import views

urlpatterns = [
    path('', views.missing_persons, name='missingpersons'),
]
