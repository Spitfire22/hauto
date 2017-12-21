from django.shortcuts import render
from .models import Make, Model, System, Manufacturer, Part

def vehicle_list(request):
    return render(request, 'vehicle/vehiclechoice.html')

def choicebar(request):
    make_choice = Make.objects.all()
    make = {'make_choice': make_choice}
    return render(request, 'vehicle/choicebar.html', make)

