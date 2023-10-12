from user import User

class Database:

    def __init__(self):
        self.__users = dict()

    def add_user(self, user):
        id = User.get_id()
        user = User(user.get_name(), user.get_age(), user.get_email())
        self.__users[id] = user
    

    def remove_user(self, id):
        self.__users.pop(id)


    def update_user(self, id):
        if id in self.__users.keys():
            new_name = input("Enter new name: ")
            new_age = int(input("Enter new age: "))
            new_email = input("Enter new email: ")
            self.__users[id].set_name(new_name)
            self.__users[id].set_age(new_age)
            self.__users[id].set_email(new_email)


    def search_users_by_name(self, name):
        suitable_users = []
        for key in self.__users.keys():
            if name.lower() in self.__users[key].get_name().lower():
                suitable_users.append(self.__users[key])

        # suitable_users = [user for user in self.__users if name in user.get_name().lower()]
        return suitable_users


    def search_users_by_age(self, age):
        suitable_users = []
        for key in self.__users.keys():
            if self.__users[key].get_age() == age:
                suitable_users.append(self.__users[key])
        return suitable_users


    def search_users_by_email(self, email):
        suitable_users = []
        for key in self.__users.keys():
            if email.lower() in self.__users[key].get_email().lower():
                suitable_users.append(self.__users[key])
        return suitable_users


    def show_info(self):
        for user_key in self.__users:
            print(f"{user_key}: {self.__users[user_key].get_name()}, {self.__users[user_key].get_age()}, {self.__users[user_key].get_email()}")