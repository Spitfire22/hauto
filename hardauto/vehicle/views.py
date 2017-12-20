from django.shortcuts import render
from .models import Make, Model, System, Manufacturer, Part

def vehicle_list(request):
    make_choice = Make.objects.all()
    context = {'make_choice': make_choice}
    return render(request, 'vehicle/vehicle_choice.html', context)

