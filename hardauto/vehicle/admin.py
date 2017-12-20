from django.contrib import admin
from .models import Make, Model, System, Manufacturer, Part

admin.site.register(Make)
admin.site.register(Model)
admin.site.register(System)
admin.site.register(Manufacturer)
admin.site.register(Part)