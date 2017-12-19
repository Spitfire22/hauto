from django.db import models

class Vehicle(models.Model):
    make = models.CharField(max_length=80)
    year = models.IntegerField(default=2000)
    carmodel = models.CharField(max_length=80)
    trim = models.CharField(max_length=80)
    engine = models.CharField(max_length=20)
    hybrid = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.year} {self.make} {self.carmodel} {self.trim} {self.engine} {self.hybrid}'

class System(models.Model):
    system = models.CharField(max_length=80)
    subsystem = models.CharField(max_length=80)

    def __str__(self):
        return f'{self.system} {self.subsystem}'

class Part(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    system = models.ForeignKey(System, on_delete=models.CASCADE)
    partname = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=80)
    partnumber = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.manufacturer} {self.partname} {self.partnumber}'