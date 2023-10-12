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
    
    def show_info(self):
        print(f"Id: {User.__id}, name: {self.__name}, age: {self.__age}, email: {self.__email}")
    

if __name__ == "__main__":
    user = User("Jacob", 0, "jacob.issakov@gmail.com")
    user.show_info()