from app.model.persons import Persons

class PersonServices:
    def __init__(self):
        pass
    
    def list_person():
        query = Persons.select()
        for person in query:
            print(f"{person.id}, {person.first_name}, {person.last_name}, {person.document_nro}")
        return query
            
    def get_person_filter(document, first_name, last_name):
        if document is not None:
            query = Persons.select().where(Persons.document_nro == document)            
        if first_name is not None:
            query = Persons.select().where(Persons.first_name == first_name)
        if last_name is not None:
            query = Persons.select().where(Persons.last_name == last_name)
            
        for person in query:
            print(f"{person.id}, {person.first_name}, {person.last_name}, {person.document_nro}")
            
            