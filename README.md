# Sistema de Gestión de Filamentos 3D

Sistema web para gestionar el stock y configuraciones de filamentos 3D, incluyendo cambios de color entre filamentos.

## Requisitos del Sistema

- Python 3.12+
- MongoDB
- Django 5.2.1
- Django-MongoEngine

## Instalación

### 1. Instalar MongoDB

```bash
sudo apt update
sudo apt install mongodb
sudo systemctl status mongodb
```

### 2. Configurar Entorno Virtual

```bash
# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

### 3. Configurar MongoDB

Editar el archivo `filament_server/settings.py`:

```python
MONGODB_DATABASES = {
    'default': {
        'name': 'filament_db',
        'host': 'localhost',
        'port': 27017,
        'username': '',
        'password': '',
        'authentication_source': 'admin',
    }
}
```

### 4. Crear Superusuario

```bash
python manage.py createsuperuser
```

## Estructura de Datos

### Modelos Principales

1. **Brand** (Marca)
   - `name`: Nombre de la marca (único)
   - `website`: URL de la web oficial

2. **Printer** (Impresora)
   - `name`: Nombre de la impresora (único)
   - `laminator_code`: Código del laminador

3. **FilamentType** (Tipo de Filamento)
   - `brand`: Referencia a Brand
   - `material`: Material del filamento
   - Índice único: marca + material

4. **Filament** (Filamento)
   - `brand`: Referencia a Brand
   - `filament_type`: Referencia a FilamentType
   - `quantity`: Cantidad disponible
   - `color`: Color del filamento
   - `ral`: Código RAL

5. **FilamentConfiguration** (Configuración)
   - `filament_type`: Referencia a FilamentType
   - `printer`: Referencia a Printer
   - `temperature`: Temperatura de extrusión
   - `flow`: Flujo de material
   - `pressure_advance`: Avance de presión
   - `retraction_distance`: Distancia de retracción
   - `bed_temperature`: Temperatura de cama
   - Índice único: tipo + impresora

6. **ColorChange** (Cambio de Color)
   - `filament_1`: Referencia a Filament
   - `filament_2`: Referencia a Filament
   - `value_1_to_2`: Valor del cambio de 1 a 2
   - `value_2_to_1`: Valor del cambio de 2 a 1
   - `printer`: Referencia a Printer
   - Índice único: filamento1 + filamento2 + impresora

## Uso de la Aplicación

### Acceso al Admin de Django

```
http://localhost:8000/admin/
```

### Interfaz de Usuario

```
http://localhost:8000/
```

### Comandos Útiles

```bash
# Iniciar el servidor
python manage.py runserver

# Hacer migraciones
python manage.py makemigrations
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Verificar estado del servidor
curl http://localhost:8000/
```

## Flujo de Trabajo

1. **Configuración Inicial**
   - Crear marcas de filamento
   - Registrar impresoras 3D
   - Definir tipos de filamento

2. **Gestión Diaria**
   - Registrar nuevos filamentos
   - Actualizar cantidades
   - Configurar impresoras
   - Documentar cambios de color

3. **Consultas**
   - Ver configuraciones por impresora
   - Consultar cambios de color
   - Filtrar filamentos disponibles

## Mantenimiento

### Backup de MongoDB

```bash
mongodump --db filament_db --out /backup/mongodb/
```

### Restauración de MongoDB

```bash
mongorestore --db filament_db /backup/mongodb/filament_db/
```

### Índices Adicionales

```bash
mongo filament_db --eval 'db.filaments.createIndex({brand: 1})'
mongo filament_db --eval 'db.filaments.createIndex({color: 1})'
```

## Licencia

MIT License
