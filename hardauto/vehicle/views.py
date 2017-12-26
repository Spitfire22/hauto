from django.shortcuts import render
from .models import Make, Model, System, Manufacturer, Part
from django.http import HttpResponse, JsonResponse

def vehicle_list(request):
    return render(request, 'vehicle/vehiclechoice.html')

def choicebar(request):
    make_choice = Make.objects.all()
    # make = {'make_choice': make_choice}
    model_choice = Model.objects.all()
    # model = {'model_choice': model_choice}
    system_choice = System.objects.all()
    # system = {'system_choice': system_choice}
    manu_choice = Manufacturer.objects.all()
    # manufacturer = {'manu_choice': manu_choice}
    part_choice = Part.objects.all()
    # part = {'part_choice': part_choice)


    all_choices = {'make_choice': make_choice, 'model_choice': model_choice, 'system_choice': system_choice,
                   'manu_choice': manu_choice, 'part_choice': part_choice}
    return render(request, 'vehicle/choicebar.html', all_choices)

def getmodels(request):
    make_id = request.GET['make_id']
    make = Make.objects.get(pk=make_id)
    models = {'models':[]}
    for model in make.model_set.all():
        models['models'].append({
            'id': model.id,
            'name': model.name,
        })
    return JsonResponse(models)

def getsystems(request):
    model_id = request.GET['model_id']
    model = Model.objects.get(pk=model_id)
    systems = {'systems':[]}
    for system in model.system_set.all():
        systems['systems'].append({
            'id': system.id,
            'name': system.name,
        })
    return JsonResponse(systems)

def getparts(request):
    system_id = request.GET['system_id']
    system = System.objects.get(pk=system_id)
    parts = {'parts':[]}
    for part in system.part_set.all():
        parts['parts'].append({
            'id': part.id,
            'name': part.name,
            'manufacturer': part.manufacturer,
            'number': part.number,
        })
    return JsonResponse(parts)

