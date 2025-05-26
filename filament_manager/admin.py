from django.contrib import admin
from mongoengine.django.mongo_admin import DocumentAdmin
from .models import Brand, Printer, FilamentType, Filament, FilamentConfiguration, ColorChange

class BrandAdmin(DocumentAdmin):
    list_display = ('name', 'website')
    search_fields = ('name',)

class PrinterAdmin(DocumentAdmin):
    list_display = ('name', 'laminator_code')
    search_fields = ('name', 'laminator_code')

class FilamentTypeAdmin(DocumentAdmin):
    list_display = ('brand', 'material')
    list_filter = ('brand',)
    search_fields = ('material',)

class FilamentAdmin(DocumentAdmin):
    list_display = ('brand', 'filament_type', 'quantity', 'color', 'ral')
    list_filter = ('brand', 'filament_type')
    search_fields = ('color', 'ral')

class FilamentConfigurationAdmin(DocumentAdmin):
    list_display = ('filament_type', 'printer', 'temperature', 'flow', 'pressure_advance', 'retraction_distance', 'bed_temperature')
    list_filter = ('filament_type', 'printer')

class ColorChangeAdmin(DocumentAdmin):
    list_display = ('filament_1', 'filament_2', 'printer', 'value_1_to_2', 'value_2_to_1')
    list_filter = ('printer',)

admin.site.register(Brand, BrandAdmin)
admin.site.register(Printer, PrinterAdmin)
admin.site.register(FilamentType, FilamentTypeAdmin)
admin.site.register(Filament, FilamentAdmin)
admin.site.register(FilamentConfiguration, FilamentConfigurationAdmin)
admin.site.register(ColorChange, ColorChangeAdmin)
