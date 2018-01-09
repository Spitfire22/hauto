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
    image = models.ImageField(upload_to='system/', width_field='width_field', height_field='height_field', null=True, blank=True)
    width_field = models.IntegerField(default=200)
    height_field = models.IntegerField(default=200)

    def __str__(self):
        return self.name

class Manufacturer(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

class Part(models.Model):
    name = models.CharField(max_length=100)
    system = models.ForeignKey(System, on_delete=models.CASCADE, related_name='part')
    relatedsystem1 = models.ForeignKey(System, on_delete=models.CASCADE, related_name='related_part1', null=True, blank=True)
    relatedsystem2 = models.ForeignKey(System, on_delete=models.CASCADE, related_name='related_part2', null=True, blank=True)
    relatedsystem3 = models.ForeignKey(System, on_delete=models.CASCADE, related_name='related_part3', null=True, blank=True)
    image = models.ImageField(upload_to='generic/', width_field='width_field', height_field='height_field', null=True, blank=True)
    width_field = models.IntegerField(default=200)
    height_field = models.IntegerField(default=200)

    def __str__(self):
        return f'{self.name}, System: {self.system.name}'



class ManufacturedPart(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    number = models.CharField(max_length=60)
    discontinued_number1 = models.CharField(max_length=60, blank=True)
    discontinued_number2 = models.CharField(max_length=60, blank=True)
    discontinued_number3 = models.CharField(max_length=60, blank=True)
    image = models.ImageField(upload_to='specific/', width_field='width_field', height_field='height_field', null=True, blank=True)
    width_field = models.IntegerField(default=200)
    height_field = models.IntegerField(default=200)
    text = models.TextField(blank=True)
    cost = models.CharField(max_length=20, blank=True)

    UNKNOWN_GRADE = 'Grade Unspecified'
    ORIGINAL_EQUIPMENT = 'Original Equipment Manufacturer'
    OE_REPLACEMENT = 'Aftermarket Replacement'
    PERFORMANCE = 'Preformance'
    RACING = 'Race Specific'
    GRADE_CHOICES = (
        (UNKNOWN_GRADE, 'N/A'),
        (ORIGINAL_EQUIPMENT, 'Original Equipment'),
        (OE_REPLACEMENT, 'OEM Replacement'),
        (PERFORMANCE, 'Street Performance'),
        (RACING, 'Racing Only'),
    )
    grade = models.CharField(
        max_length=20,
        choices=GRADE_CHOICES,
        default=UNKNOWN_GRADE,
    )

    def __str__(self):
        return f'{self.part.name} #: {self.number}  -  Mfg: {self.manufacturer.name}'



