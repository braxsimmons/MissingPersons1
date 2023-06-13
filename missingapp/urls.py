from django.urls import path
from missingapp import views

urlpatterns = [
    path('table/', views.missing_persons, name='missingpersons'),
    path('', views.landingpageview)
]
