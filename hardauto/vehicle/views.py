from django.shortcuts import render
from .models import Make, Model, System, Manufacturer, Part, ManufacturedPart
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
    # part = {'part_choice': part_choice}
    manufacturedpart_choice = ManufacturedPart.objects.all()
    # manufacturedpart = {'manufacturedpart_choice': manufacturedpart_choice}


    all_choices = {'make_choice': make_choice, 'model_choice': model_choice, 'system_choice': system_choice,
                   'manu_choice': manu_choice, 'part_choice': part_choice,
                   'manufacturedpart_choice': manufacturedpart_choice}
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
    for part in system.part.all():
        parts['parts'].append({
            'id': part.id,
            'name': part.name,
            'relatedsystem1': part.relatedsystem1.name if part.relatedsystem1 else '',
            'relatedsystem2': part.relatedsystem2.name if part.relatedsystem2 else '',
            'relatedsystem3': part.relatedsystem3.name if part.relatedsystem3 else '',
        })
    return JsonResponse(parts)

def getmanufacturedparts(request):
    part_id = request.GET['part_id']
    part = Part.objects.get(pk=part_id)
    manufacturedparts = {'manufacturedparts':[]}
    for manufacturedpart in part.manufacturedpart_set.all():
        manufacturedparts['manufacturedparts'].append({
            'id': manufacturedpart.id,
            'manufacturer': manufacturedpart.manufacturer.name,
            'number': manufacturedpart.number,
            'discontinued_number1': manufacturedpart.discontinued_number1,
            'discontinued_number2': manufacturedpart.discontinued_number2,
            'discontinued_number3': manufacturedpart.discontinued_number3,
            'text': manufacturedpart.text,
            'cost': manufacturedpart.cost,
            'grade': manufacturedpart.grade,
        })
    return JsonResponse(manufacturedparts)