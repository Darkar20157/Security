from peewee import *
from datetime import datetime

route_database = 'C:\ProyectoDanny\Security\data\db.db'
db = SqliteDatabase(route_database)

class Persons(Model):
    id = AutoField(primary_key=True)
    active = BooleanField()
    register_date = DateTimeField()
    update_date = DateTimeField(null=True)
    document_nro = CharField(unique=True)
    type_document = CharField(null=True)
    first_name = CharField()
    last_name = CharField()
    phone = CharField(null=True)
    email = CharField(null=True)
    age = DateTimeField(null=True)
    location = CharField(null=True)
    
    class Meta:
        database = db
        
models = [Persons]
try:
    with db:
        db.create_tables(models)
        print("tabla Person fue creada correctamente")
except OperationalError as e:
    print(f"Error al conectar a la base de datos: {e}")
    
    
# persons_data = [
#     {
#         'active': True,
#         'register_date': datetime.now(),
#         'update_date': datetime.now(),
#         'document_nro': '1234567890',
#         'type_document': 'DNI',
#         'first_name': 'Juan',
#         'last_name': 'Pérez',
#         'phone': '123-456-789',
#         'email': 'juan@example.com',
#     },
#     {
#         'active': True,
#         'register_date': datetime.now(),
#         'update_date': datetime.now(),
#         'document_nro': '0987654321',
#         'type_document': 'Pasaporte',
#         'first_name': 'María',
#         'last_name': 'Gómez',
#         'phone': '987-654-321',
#         'email': 'maria@example.com',
#     },
#     {
#         'active': True,
#         'register_date': datetime.now(),
#         'update_date': datetime.now(),
#         'document_nro': '2468013579',
#         'type_document': 'DNI',
#         'first_name': 'Pedro',
#         'last_name': 'Martínez',
#         'phone': '456-789-123',
#         'email': 'pedro@example.com',
#     },
#     {
#         'active': True,
#         'register_date': datetime.now(),
#         'update_date': datetime.now(),
#         'document_nro': '9876543210',
#         'type_document': 'Pasaporte',
#         'first_name': 'Ana',
#         'last_name': 'López',
#         'phone': '789-123-456',
#         'email': 'ana@example.com',
#     },
#     {
#         'active': True,
#         'register_date': datetime.now(),
#         'update_date': datetime.now(),
#         'document_nro': '5678901234',
#         'type_document': 'DNI',
#         'first_name': 'Luis',
#         'last_name': 'González',
#         'phone': '654-987-321',
#         'email': 'luis@example.com',
#     },
#     {
#         'active': True,
#         'register_date': datetime.now(),
#         'update_date': datetime.now(),
#         'document_nro': '4321098765',
#         'type_document': 'Pasaporte',
#         'first_name': 'Elena',
#         'last_name': 'Hernández',
#         'phone': '987-321-654',
#         'email': 'elena@example.com',
#     },
#     {
#         'active': True,
#         'register_date': datetime.now(),
#         'update_date': datetime.now(),
#         'document_nro': '6543210987',
#         'type_document': 'DNI',
#         'first_name': 'Javier',
#         'last_name': 'Sánchez',
#         'phone': '321-987-654',
#         'email': 'javier@example.com',
#     },
#     {
#         'active': True,
#         'register_date': datetime.now(),
#         'update_date': datetime.now(),
#         'document_nro': '7890123456',
#         'type_document': 'Pasaporte',
#         'first_name': 'Sofía',
#         'last_name': 'Gutiérrez',
#         'phone': '987-654-321',
#         'email': 'sofia@example.com',
#     },
#     {
#         'active': True,
#         'register_date': datetime.now(),
#         'update_date': datetime.now(),
#         'document_nro': '0123456789',
#         'type_document': 'DNI',
#         'first_name': 'Diego',
#         'last_name': 'Navarro',
#         'phone': '654-321-987',
#         'email': 'diego@example.com',
#     },
#     {
#         'active': True,
#         'register_date': datetime.now(),
#         'update_date': datetime.now(),
#         'document_nro': '1357924680',
#         'type_document': 'Pasaporte',
#         'first_name': 'Carla',
#         'last_name': 'Rojas',
#         'phone': '321-654-987',
#         'email': 'carla@example.com',
#     },
# ]

# for person in persons_data:
#     Persons.create(**person)
#     print(person)