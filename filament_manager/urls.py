from django.urls import path
from . import views

app_name = 'filament_manager'

urlpatterns = [
    path('', views.index, name='index'),
    
    # Marcas
    path('brands/', views.brand_list, name='brand_list'),
    path('brands/create/', views.brand_create, name='brand_create'),
    path('brands/<str:id>/edit/', views.brand_edit, name='brand_edit'),
    path('brands/<str:id>/delete/', views.brand_delete, name='brand_delete'),
    
    # Impresoras
    path('printers/', views.printer_list, name='printer_list'),
    path('printers/create/', views.printer_create, name='printer_create'),
    
    # Tipos de filamento
    path('filament-types/', views.filament_type_list, name='filament_type_list'),
    path('filament-types/create/', views.filament_type_create, name='filament_type_create'),
    
    # Filamentos
    path('filaments/', views.filament_list, name='filament_list'),
    path('filaments/create/', views.filament_create, name='filament_create'),
    
    # Configuraciones de filamento
    path('filament-configurations/', views.filament_configuration_list, name='filament_configuration_list'),
    path('filament-configurations/create/', views.filament_configuration_create, name='filament_configuration_create'),
    path('filament-configurations/<int:printer_id>/', views.get_filament_configurations, name='filament_configurations'),
    
    # Cambios de color
    path('color-changes/', views.color_change_list, name='color_change_list'),
    path('color-changes/create/', views.color_change_create, name='color_change_create'),
    path('color-changes/<int:printer_id>/', views.get_filament_color_changes, name='filament_color_changes'),
]
