from django.db import models

class Vehicle(models.Model):
    manufacturer = models.CharField(max_length=80)
    year = models.IntegerField(default=2000)
    carmodel = models.CharField(max_length=80)
    trim = models.CharField(max_length=80)
    engine = models.CharField(max_length=20)
    hybrid = models.BooleanField(default=False)
