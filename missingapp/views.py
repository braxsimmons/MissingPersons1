from django.shortcuts import render
from .models import Person

def missing_persons(request):
    personList = Person.objects.all()
    context = {
        'persons': personList
    }

    return render(request, "missingapp/missingpersons.html", context)

def landingpageview(request):
    return render(request, "missingapp/landingpage.html")

def person_details(request):
    data = Person.objects.filter(
        id=personId
    ).get()
    context = {
        'persondetails': data
    }
    return render(request, "missingapp/persondetails.html", context)
