from datetime import datetime
from peewee import IntegrityError, OperationalError
import app.utils.generic as utl
from app.model.persons import Persons

class PersonServices:
    def __init__(self):
        pass
    
    def list_person():
        persons = list(Persons);
        query = Persons.select()
        return query
            
    def get_person_filter(document, first_name, last_name):
        query = Persons.select()
        if document:
            query = query.where(Persons.document_nro == document)            
        if first_name:
            query = query.where(Persons.first_name == first_name)
        if last_name:
            query = query.where(Persons.last_name == last_name)
            
        print(f"Se encontro :{query.count()}")
        person = query.first()
        return person
    
    
    #Ajustar logica al momento de guardar el Person
    def save_person(document_nro, type_document, first_name, last_name, phone, email, age, location):
        try:
            if document_nro is None and len(document_nro) > 12 and int(document_nro):
                raise ValueError(f"El documento no es valido: {document_nro}")
            
            if type_document is None:
                raise ValueError(f"El tipo de documento no es valido: {type_document}")
                
            if first_name is None and len(first_name) > 255:
                raise ValueError(f"El nombre no es valido: {first_name}")
                
            if last_name is None and len(last_name) > 255:
                raise ValueError(f"El nombre no es valido: {last_name}")
                
            if phone is not None and len(phone) > 10:
                raise ValueError(f"El celular no es valido: {phone}")
            
            if email is not None and not utl.valid_email(email):
                raise ValueError(f"El email no es valido: {phone}")
                
            if age is not None:
                raise ValueError(f"La fecha de nacimiento no es valido: {phone}")
            
            if location is not None and len(location) > 255:
                raise ValueError(f"La direccion no es valido: {phone}")
            person = Persons.create(active = True, register_date = datetime.now(), document_nro = document_nro, type_document = type_document, first_name = first_name, 
                                    last_name = last_name, phone = phone, email = email, age = age, location = location)
            return person
        except IntegrityError as e:
            raise ValueError(f"El usuario ya fue guardado: {e}")
        except OperationalError as e:
            raise ValueError(f"Error operativo: {e}")
        except ValueError as ve:
            raise ValueError(ve)
        except Exception as e:
            raise ValueError(f"Se produjo un error inesperado: {e}")