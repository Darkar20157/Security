from peewee import *
from app.model.users import Users

class UsersServices:
    def __init__(self):
        pass
    
    def login(user_name, password):
        if user_name is not None and password is not None:
            try:
                user = Users.get(Users.user_name == user_name)
                if user is not None:
                    if(user.password == password):
                        return user
                    else:   
                        return False
                return False
            except Users.DoesNotExist as exist:
                return "instance matching query does not exist"
            except Exception as e:
                return e
    