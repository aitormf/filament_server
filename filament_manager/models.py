from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False)
    website = models.CharField(max_length=200, blank=True, null=True)

class Printer(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False)
    laminator_code = models.CharField(max_length=50, blank=False)

class FilamentType(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=False)
    material = models.CharField(max_length=100, blank=False)

    class Meta:
        unique_together = ('brand', 'material')

class Filament(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=False)
    filament_type = models.ForeignKey(FilamentType, on_delete=models.CASCADE, blank=False)
    quantity = models.IntegerField(blank=False)
    color = models.CharField(max_length=100, blank=False)
    ral = models.CharField(max_length=10, blank=True, null=True)

class FilamentConfiguration(models.Model):
    filament_type = models.ForeignKey(FilamentType, on_delete=models.CASCADE, blank=False)
    printer = models.ForeignKey(Printer, on_delete=models.CASCADE, blank=False)
    temperature = models.FloatField(blank=False)
    flow = models.FloatField(blank=False)
    pressure_advance = models.FloatField(blank=False)
    retraction_distance = models.FloatField(blank=False)
    bed_temperature = models.FloatField(blank=False)

    class Meta:
        unique_together = ('filament_type', 'printer')

class ColorChange(models.Model):
    filament_1 = models.ForeignKey(Filament, on_delete=models.CASCADE, blank=False, related_name='color_change_filament_1')
    filament_2 = models.ForeignKey(Filament, on_delete=models.CASCADE, blank=False, related_name='color_change_filament_2')
    value_1_to_2 = models.FloatField(blank=False)
    value_2_to_1 = models.FloatField(blank=False)
    printer = models.ForeignKey(Printer, on_delete=models.CASCADE, blank=False)

    class Meta:
        unique_together = ('filament_1', 'filament_2', 'printer')
