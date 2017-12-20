from django.db import models


class Make(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

class Model(models.Model):
    name = models.CharField(max_length=80)
    make = models.ForeignKey(Make, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class System(models.Model):
    name = models.CharField(max_length=100)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Manufacturer(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

class Part(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    system = models.ForeignKey(System,  on_delete=models.CASCADE)
    number = models.CharField(max_length=60)

    def __str__(self):
        return f'Manufacturer: {self.manufacturer}, Part Name: {self.name}, Part Number: {self.number}'
