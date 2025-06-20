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

class ColorChangeForm(forms.Form):
    filament_1 = forms.ChoiceField(label='Filamento 1')
    filament_2 = forms.ChoiceField(label='Filamento 2')
    printer = forms.ChoiceField(label='Impresora')
    value_1_to_2 = forms.FloatField(label='Valor 1→2')
    value_2_to_1 = forms.FloatField(label='Valor 2→1')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['filament_1'].choices = []
        self.fields['filament_2'].choices = []
        self.fields['printer'].choices = []
