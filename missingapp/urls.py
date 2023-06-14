from django.urls import path
from missingapp import views

urlpatterns = [
    path('table/', views.missing_persons, name='missingpersons'),
    path('', views.landingpageview),
    path('table/<str:first_name>/', views.person_details, name='person_details')
]
