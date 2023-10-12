class NameDescriptor:

    def __get__(self, instance, owner):
        return instance.__name

    def __set__(self, instance, value):
        if value.isalpha(): 
            instance.__name = value
        else:
            raise ValueError("Name must contain only letters")


class AgeDescriptor:

    def __get__(self, instance, owner):
        return instance.__age
    
    def __set__(self, instance, value):
        if value > 0:
            instance.__age = value
        else:
            raise ValueError("Age must be greater than zero")


class EmailDescriptor:

    def __get__(self, instance, owner):
        return instance.__email

    def __set__(self, instance, value):
        if "@" in value:
            instance.__email = value
        else:
            raise ValueError("Email must contain such symbol '@'")
        

class User:
    __id = 0
    __name = NameDescriptor()
    __age = AgeDescriptor()
    __email = EmailDescriptor()

    def __init__(self, name, age, email):
        self.__name = name
        self.__age = age
        self.__email = email
        User.increase_id()


    @classmethod
    def increase_id(cls):
        cls.__id += 1
        return User.__id
    

    @staticmethod
    def get_id():
        return User.__id
    

    def get_name(self):
        return self.__name
    

    def set_name(self, name):
        self.__name = name
    

    def get_age(self):
        return self.__age
    

    def set_age(self, age):
        self.__age = age
    
    
    def get_email(self):
        return self.__email
    

    def set_email(self, email):
        self.__email = email
        
    
    
    def show_info(self):
        print(f"Name: {self.__name}, Age: {self.__age}, Email: {self.__email}")
    
