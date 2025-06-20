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
            return redirect('filament_manager:brand_list')
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
            return redirect('filament_manager:brand_list')
    else:
        form = BrandForm(instance=brand)
    return render(request, 'filament_manager/brand_form.html', {'form': form, 'brand': brand})

def brand_delete(request, id):
    brand = get_object_or_404(Brand, id=id)
    if request.method == 'POST':
        brand.delete()
        messages.success(request, 'Marca eliminada exitosamente')
        return redirect('filament_manager:brand_list')
    return render(request, 'filament_manager/confirm_delete.html', {
        'object': brand,
        'object_name': 'marca',
        'redirect_url': 'filament_manager:brand_list'
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
            return redirect('filament_manager:printer_list')
    else:
        form = PrinterForm()
    return render(request, 'filament_manager/printer_form.html', {'form': form})

def printer_edit(request, id):
    printer = get_object_or_404(Printer, id=id)
    if request.method == 'POST':
        form = PrinterForm(request.POST, instance=printer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Impresora actualizada exitosamente')
            return redirect('filament_manager:printer_list')
    else:
        form = PrinterForm(instance=printer)
    return render(request, 'filament_manager/printer_form.html', {
        'form': form,
        'printer': printer,
        'title': 'Editar Impresora'
    })

def printer_delete(request, id):
    printer = get_object_or_404(Printer, id=id)
    if request.method == 'POST':
        printer.delete()
        messages.success(request, 'Impresora eliminada exitosamente')
        return redirect('filament_manager:printer_list')
    return render(request, 'filament_manager/confirm_delete.html', {
        'object': printer,
        'object_name': 'impresora',
        'redirect_url': 'filament_manager:printer_list'
    })

def filament_type_list(request):
    filament_types = FilamentType.objects.all()
    return render(request, 'filament_manager/filament_type_list.html', {'filament_types': filament_types})

def filament_type_create(request):
    if request.method == 'POST':
        form = FilamentTypeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tipo de filamento creado exitosamente')
            return redirect('filament_manager:filament_type_list')
    else:
        form = FilamentTypeForm()
    return render(request, 'filament_manager/filament_type_form.html', {'form': form})

def filament_type_edit(request, id):
    filament_type = get_object_or_404(FilamentType, id=id)
    if request.method == 'POST':
        form = FilamentTypeForm(request.POST, instance=filament_type)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tipo de filamento actualizado exitosamente')
            return redirect('filament_manager:filament_type_list')
    else:
        form = FilamentTypeForm(instance=filament_type)
    return render(request, 'filament_manager/filament_type_form.html', {
        'form': form,
        'filament_type': filament_type,
        'title': 'Editar Tipo de Filamento'
    })

def filament_type_delete(request, id):
    filament_type = get_object_or_404(FilamentType, id=id)
    if request.method == 'POST':
        filament_type.delete()
        messages.success(request, 'Tipo de filamento eliminado exitosamente')
        return redirect('filament_manager:filament_type_list')
    return render(request, 'filament_manager/confirm_delete.html', {
        'object': filament_type,
        'object_name': 'tipo de filamento',
        'redirect_url': 'filament_manager:filament_type_list'
    })

def filament_list(request):
    filaments = Filament.objects.all()
    return render(request, 'filament_manager/filament_list.html', {'filaments': filaments})

def filament_create(request):
    if request.method == 'POST':
        form = FilamentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Filamento creado exitosamente')
            return redirect('filament_manager:filament_list')
    else:
        form = FilamentForm()
    return render(request, 'filament_manager/filament_form.html', {'form': form})

def filament_edit(request, id):
    filament = get_object_or_404(Filament, id=id)
    if request.method == 'POST':
        form = FilamentForm(request.POST, instance=filament)
        if form.is_valid():
            form.save()
            messages.success(request, 'Filamento actualizado exitosamente')
            return redirect('filament_manager:filament_list')
    else:
        form = FilamentForm(instance=filament)
    return render(request, 'filament_manager/filament_form.html', {
        'form': form,
        'filament': filament,
        'title': 'Editar Filamento'
    })

def filament_delete(request, id):
    filament = get_object_or_404(Filament, id=id)
    if request.method == 'POST':
        filament.delete()
        messages.success(request, 'Filamento eliminado exitosamente')
        return redirect('filament_manager:filament_list')
    return render(request, 'filament_manager/confirm_delete.html', {
        'object': filament,
        'object_name': 'filamento',
        'redirect_url': 'filament_manager:filament_list'
    })

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
            return redirect('filament_manager:filament_configuration_list')
    else:
        form = FilamentConfigurationForm()
    return render(request, 'filament_manager/filament_configuration_form.html', {'form': form})

def filament_configuration_edit(request, id):
    configuration = get_object_or_404(FilamentConfiguration, id=id)
    if request.method == 'POST':
        form = FilamentConfigurationForm(request.POST, instance=configuration)
        if form.is_valid():
            form.save()
            messages.success(request, 'Configuración actualizada exitosamente')
            return redirect('filament_manager:filament_configuration_list')
    else:
        form = FilamentConfigurationForm(instance=configuration)
    return render(request, 'filament_manager/filament_configuration_form.html', {
        'form': form,
        'configuration': configuration,
        'title': 'Editar Configuración'
    })

def filament_configuration_delete(request, id):
    configuration = get_object_or_404(FilamentConfiguration, id=id)
    if request.method == 'POST':
        configuration.delete()
        messages.success(request, 'Configuración eliminada exitosamente')
        return redirect('filament_manager:filament_configuration_list')
    return render(request, 'filament_manager/confirm_delete.html', {
        'object': configuration,
        'object_name': 'configuración',
        'redirect_url': 'filament_manager:filament_configuration_list'
    })

def color_change_list(request):
    color_changes = ColorChange.objects.all()
    return render(request, 'filament_manager/color_change_list.html', {
        'color_changes': color_changes,
        'Filament': Filament,
        'Printer': Printer
    })

def color_change_create(request):
    if request.method == 'POST':
        form = ColorChangeForm(request.POST)
        if form.is_valid():
            # Crear el cambio de color
            color_change = ColorChange.objects.create(
                filament_1=form.cleaned_data['filament_1'],
                filament_2=form.cleaned_data['filament_2'],
                printer=form.cleaned_data['printer'],
                value_1_to_2=form.cleaned_data['value_1_to_2'],
                value_2_to_1=form.cleaned_data['value_2_to_1']
            )
            messages.success(request, 'Cambio de color creado exitosamente')
            return redirect('filament_manager:color_change_list')
    else:
        # Cargar datos para los ChoiceFields
        filaments = Filament.objects.all()
        printers = Printer.objects.all()
        
        form = ColorChangeForm()
        form.fields['filament_1'].choices = [(f.id, f.brand.name + ' - ' + f.color) for f in filaments]
        form.fields['filament_2'].choices = [(f.id, f.brand.name + ' - ' + f.color) for f in filaments]
        form.fields['printer'].choices = [(p.id, p.name) for p in printers]
    return render(request, 'filament_manager/color_change_form.html', {'form': form})

def color_change_edit(request, id):
    color_change = get_object_or_404(ColorChange, id=id)
    
    # Cargar datos para los ChoiceFields
    filaments = Filament.objects.all()
    printers = Printer.objects.all()
    
    if request.method == 'POST':
        form = ColorChangeForm(request.POST)
        if form.is_valid():
            # Actualizar el cambio de color
            ColorChange.objects.filter(id=id).update(
                filament_1_id=form.cleaned_data['filament_1'],
                filament_2_id=form.cleaned_data['filament_2'],
                printer_id=form.cleaned_data['printer'],
                value_1_to_2=form.cleaned_data['value_1_to_2'],
                value_2_to_1=form.cleaned_data['value_2_to_1']
            )
            messages.success(request, 'Cambio de color actualizado exitosamente')
            return redirect('filament_manager:color_change_list')
    else:
        # Crear formulario con los valores actuales
        form = ColorChangeForm(initial={
            'filament_1': color_change.filament_1_id,
            'filament_2': color_change.filament_2_id,
            'printer': color_change.printer_id,
            'value_1_to_2': color_change.value_1_to_2,
            'value_2_to_1': color_change.value_2_to_1
        })
        
        # Cargar opciones para los ChoiceFields
        form.fields['filament_1'].choices = [(f.id, f.brand.name + ' - ' + f.color) for f in filaments]
        form.fields['filament_2'].choices = [(f.id, f.brand.name + ' - ' + f.color) for f in filaments]
        form.fields['printer'].choices = [(p.id, p.name) for p in printers]
    
    return render(request, 'filament_manager/color_change_form.html', {
        'form': form,
        'color_change': color_change,
        'title': 'Editar Cambio de Color'
    })

def color_change_delete(request, id):
    color_change = get_object_or_404(ColorChange, id=id)
    if request.method == 'POST':
        color_change.delete()
        messages.success(request, 'Cambio de color eliminado exitosamente')
        return redirect('filament_manager:color_change_list')
    return render(request, 'filament_manager/confirm_delete.html', {
        'object': color_change,
        'object_name': 'cambio de color',
        'redirect_url': 'filament_manager:color_change_list'
    })

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
