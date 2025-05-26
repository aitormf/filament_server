from mongoengine import Document, StringField, FloatField, IntField, ReferenceField, ListField

class Brand(Document):
    name = StringField(required=True, unique=True)
    website = StringField()

class Printer(Document):
    name = StringField(required=True, unique=True)
    laminator_code = StringField(required=True)

class FilamentType(Document):
    brand = ReferenceField(Brand, required=True)
    material = StringField(required=True)
    meta = {
        'indexes': [
            {'fields': ['brand', 'material'], 'unique': True}
        ]
    }

class Filament(Document):
    brand = ReferenceField(Brand, required=True)
    filament_type = ReferenceField(FilamentType, required=True)
    quantity = IntField(required=True)
    color = StringField(required=True)
    ral = StringField()

class FilamentConfiguration(Document):
    filament_type = ReferenceField(FilamentType, required=True)
    printer = ReferenceField(Printer, required=True)
    temperature = FloatField(required=True)
    flow = FloatField(required=True)
    pressure_advance = FloatField(required=True)
    retraction_distance = FloatField(required=True)
    bed_temperature = FloatField(required=True)
    meta = {
        'indexes': [
            {'fields': ['filament_type', 'printer'], 'unique': True}
        ]
    }

class ColorChange(Document):
    filament_1 = ReferenceField(Filament, required=True)
    filament_2 = ReferenceField(Filament, required=True)
    value_1_to_2 = FloatField(required=True)
    value_2_to_1 = FloatField(required=True)
    printer = ReferenceField(Printer, required=True)
    meta = {
        'indexes': [
            {'fields': ['filament_1', 'filament_2', 'printer'], 'unique': True}
        ]
    }
