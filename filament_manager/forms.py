from django import forms
from .models import Brand, Printer, FilamentType, Filament, FilamentConfiguration, ColorChange

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name', 'website']

class PrinterForm(forms.ModelForm):
    class Meta:
        model = Printer
        fields = ['name', 'laminator_code']

class FilamentTypeForm(forms.ModelForm):
    class Meta:
        model = FilamentType
        fields = ['brand', 'material']

class FilamentForm(forms.ModelForm):
    class Meta:
        model = Filament
        fields = ['brand', 'filament_type', 'quantity', 'color', 'ral']

class FilamentConfigurationForm(forms.ModelForm):
    class Meta:
        model = FilamentConfiguration
        fields = ['filament_type', 'printer', 'temperature', 'flow', 'pressure_advance', 'retraction_distance', 'bed_temperature']

class ColorChangeForm(forms.ModelForm):
    class Meta:
        model = ColorChange
        fields = ['filament_1', 'filament_2', 'printer', 'value_1_to_2', 'value_2_to_1']
