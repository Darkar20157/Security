from peewee import *
from datetime import datetime

route_database = 'C:\ProyectoDanny\Security\data\db.db'
db = SqliteDatabase(route_database)

class Users(Model):
    id = AutoField(primary_key=True)
    active = BooleanField()
    register_date = DateTimeField()
    update_date = DateTimeField()
    user_name = CharField()
    password = CharField()
    document_nro = CharField(unique=True, null=True)
    type_document = CharField(null=True)
    first_name = CharField(null=True)
    last_name = CharField(null=True)
    phone = CharField(null=True)
    email = CharField(null=True)
    
    class Meta:
        database = db
        
models = [Users]
try:
    with db:
        db.create_tables(models)
        print("tablas creadas correctamente")
except OperationalError as e:
    print(f"Error al conectar a la base de datos: {e}")
    
    
# Lista de usuarios a crear
# usuarios = [
#     {
#         'active': True,
#         'register_date': datetime.now(),
#         'update_date': datetime.now(),
#         'user_name': 'usuario3',
#         'password': 'password789',
#         'document_nro': '1357924680',
#         'type_document': 'DNI',
#         'first_name': 'Carlos',
#         'last_name': 'Martínez',
#         'phone': '456-789-123',
#         'email': 'usuario3@example.com'
#     },
#     {
#         'active': True,
#         'register_date': datetime.now(),
#         'update_date': datetime.now(),
#         'user_name': 'usuario4',
#         'password': 'passwordabc',
#         'document_nro': '2468013579',
#         'type_document': 'Pasaporte',
#         'first_name': 'Ana',
#         'last_name': 'López',
#         'phone': '789-123-456',
#         'email': 'usuario4@example.com'
#     },
#     {
#         'active': True,
#         'register_date': datetime.now(),
#         'update_date': datetime.now(),
#         'user_name': 'usuario5',
#         'password': 'passwordxyz',
#         'document_nro': '9876543210',
#         'type_document': 'DNI',
#         'first_name': 'Pedro',
#         'last_name': 'García',
#         'phone': '321-654-987',
#         'email': 'usuario5@example.com'
#     },
#     {
#         'active': True,
#         'register_date': datetime.now(),
#         'update_date': datetime.now(),
#         'user_name': 'usuario6',
#         'password': 'password123',
#         'document_nro': '5678901234',
#         'type_document': 'Pasaporte',
#         'first_name': 'Luisa',
#         'last_name': 'Rodríguez',
#         'phone': '654-987-321',
#         'email': 'usuario6@example.com'
#     },
#     {
#         'active': True,
#         'register_date': datetime.now(),
#         'update_date': datetime.now(),
#         'user_name': 'usuario7',
#         'password': 'password456',
#         'document_nro': '4321098765',
#         'type_document': 'DNI',
#         'first_name': 'Elena',
#         'last_name': 'Hernández',
#         'phone': '987-321-654',
#         'email': 'usuario7@example.com'
#     },
#     {
#         'active': True,
#         'register_date': datetime.now(),
#         'update_date': datetime.now(),
#         'user_name': 'usuario8',
#         'password': 'password789',
#         'document_nro': '6543210987',
#         'type_document': 'Pasaporte',
#         'first_name': 'Javier',
#         'last_name': 'Sánchez',
#         'phone': '321-987-654',
#         'email': 'usuario8@example.com'
#     },
#     {
#         'active': True,
#         'register_date': datetime.now(),
#         'update_date': datetime.now(),
#         'user_name': 'usuario9',
#         'password': 'passwordabc',
#         'document_nro': '7890123456',
#         'type_document': 'DNI',
#         'first_name': 'Sofía',
#         'last_name': 'Gutiérrez',
#         'phone': '987-654-321',
#         'email': 'usuario9@example.com'
#     },
#     {
#         'active': True,
#         'register_date': datetime.now(),
#         'update_date': datetime.now(),
#         'user_name': 'usuario10',
#         'password': 'passwordxyz',
#         'document_nro': '0123456789',
#         'type_document': 'Pasaporte',
#         'first_name': 'Diego',
#         'last_name': 'Navarro',
#         'phone': '654-321-987',
#         'email': 'usuario10@example.com'
#     },
# ]

# for usuario in usuarios:
#     Users.create(**usuario)
#     print(f"1#- {usuario}")