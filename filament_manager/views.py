from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Brand, Printer, FilamentType, Filament, FilamentConfiguration, ColorChange
from .forms import BrandForm, PrinterForm, FilamentTypeForm, FilamentForm, FilamentConfigurationForm, ColorChangeForm

def index(request):
    return render(request, 'filament_manager/index.html')

def brand_list(request):
    brands = Brand.objects.all()
    return render(request, 'filament_manager/brand_list.html', {'brands': brands})

def brand_create(request):
    if request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Marca creada exitosamente')
            return redirect('brand_list')
    else:
        form = BrandForm()
    return render(request, 'filament_manager/brand_form.html', {'form': form})

def brand_edit(request, id):
    brand = get_object_or_404(Brand, id=id)
    if request.method == 'POST':
        form = BrandForm(request.POST, instance=brand)
        if form.is_valid():
            form.save()
            messages.success(request, 'Marca actualizada exitosamente')
            return redirect('brand_list')
    else:
        form = BrandForm(instance=brand)
    return render(request, 'filament_manager/brand_form.html', {'form': form, 'brand': brand})

def brand_delete(request, id):
    brand = get_object_or_404(Brand, id=id)
    if request.method == 'POST':
        brand.delete()
        messages.success(request, 'Marca eliminada exitosamente')
        return redirect('brand_list')
    return render(request, 'filament_manager/confirm_delete.html', {
        'object': brand,
        'object_name': 'marca',
        'redirect_url': 'brand_list'
    })

def printer_list(request):
    printers = Printer.objects.all()
    return render(request, 'filament_manager/printer_list.html', {'printers': printers})

def printer_create(request):
    if request.method == 'POST':
        form = PrinterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Impresora creada exitosamente')
            return redirect('printer_list')
    else:
        form = PrinterForm()
    return render(request, 'filament_manager/printer_form.html', {'form': form})

def filament_type_list(request):
    filament_types = FilamentType.objects.all()
    return render(request, 'filament_manager/filament_type_list.html', {'filament_types': filament_types})

def filament_type_create(request):
    if request.method == 'POST':
        form = FilamentTypeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tipo de filamento creado exitosamente')
            return redirect('filament_type_list')
    else:
        form = FilamentTypeForm()
    return render(request, 'filament_manager/filament_type_form.html', {'form': form})

def filament_list(request):
    filaments = Filament.objects.all()
    return render(request, 'filament_manager/filament_list.html', {'filaments': filaments})

def filament_create(request):
    if request.method == 'POST':
        form = FilamentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Filamento creado exitosamente')
            return redirect('filament_list')
    else:
        form = FilamentForm()
    return render(request, 'filament_manager/filament_form.html', {'form': form})

def filament_configuration_list(request):
    printers = Printer.objects.all()
    brands = Brand.objects.all()
    filament_types = FilamentType.objects.all()
    
    printer_id = request.GET.get('printer')
    brand_id = request.GET.get('brand')
    filament_type_id = request.GET.get('filament_type')
    
    configurations = FilamentConfiguration.objects.all()
    
    if printer_id:
        configurations = configurations.filter(printer=printer_id)
    if brand_id:
        configurations = configurations.filter(filament_type__brand=brand_id)
    if filament_type_id:
        configurations = configurations.filter(filament_type=filament_type_id)
    
    return render(request, 'filament_manager/filament_configuration_list.html', {
        'configurations': configurations,
        'printers': printers,
        'brands': brands,
        'filament_types': filament_types,
        'selected_printer': printer_id,
        'selected_brand': brand_id,
        'selected_filament_type': filament_type_id
    })

def filament_configuration_create(request):
    if request.method == 'POST':
        form = FilamentConfigurationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Configuración creada exitosamente')
            return redirect('filament_configuration_list')
    else:
        form = FilamentConfigurationForm()
    return render(request, 'filament_manager/filament_configuration_form.html', {'form': form})

def color_change_list(request):
    color_changes = ColorChange.objects.all()
    return render(request, 'filament_manager/color_change_list.html', {'color_changes': color_changes})

def color_change_create(request):
    if request.method == 'POST':
        form = ColorChangeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cambio de color creado exitosamente')
            return redirect('color_change_list')
    else:
        form = ColorChangeForm()
    return render(request, 'filament_manager/color_change_form.html', {'form': form})

def get_filament_configurations(request, printer_id):
    printer = get_object_or_404(Printer, id=printer_id)
    configurations = FilamentConfiguration.objects.filter(printer=printer)
    return render(request, 'filament_manager/filament_configurations.html', {
        'printer': printer,
        'configurations': configurations
    })

def get_filament_color_changes(request, printer_id):
    printer = get_object_or_404(Printer, id=printer_id)
    color_changes = ColorChange.objects.filter(printer=printer)
    
    # Obtener todos los filamentos únicos
    unique_filaments = Filament.objects.distinct()
    
    # Crear un diccionario para mapear los cambios de color
    color_changes_dict = {}
    for change in color_changes:
        if change.filament_1.id not in color_changes_dict:
            color_changes_dict[change.filament_1.id] = {}
        if change.filament_2.id not in color_changes_dict:
            color_changes_dict[change.filament_2.id] = {}
        
        color_changes_dict[change.filament_1.id][change.filament_2.id] = change
        color_changes_dict[change.filament_2.id][change.filament_1.id] = change
    
    return render(request, 'filament_manager/filament_color_changes.html', {
        'printer': printer,
        'color_changes': color_changes_dict,
        'unique_filaments': unique_filaments
    })
