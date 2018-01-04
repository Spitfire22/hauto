from django.contrib import admin
from .models import Make, Model, System, Manufacturer, Part, ManufacturedPart


class PartAdmin(admin.ModelAdmin):
    ordering = ['name']

class ManufacturedPartAdmin(admin.ModelAdmin):
    ordering = ['manufacturer']

admin.site.register(Make)
admin.site.register(Model)
admin.site.register(System)
admin.site.register(Manufacturer)
admin.site.register(Part, PartAdmin)
admin.site.register(ManufacturedPart, ManufacturedPartAdmin)

