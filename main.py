from database import Database
from user import User

if __name__ == "__main__":
    db = Database()
    db.add_user(User("Jacob", 17, "jacob.issakov@gmail.com"))
    db.add_user(User("Den", 20, "den@gmail.com"))
    db.add_user(User("Alexandra", 21, "alexandra@gmail.com"))
    db.add_user(User("Alex", 21, "alex@gmail.com"))
    db.add_user(User("Vlad", 18, "vlad@gmail.com"))
    db.show_info()
    print("\n___________________________________________________________________\n")
    # db.remove_user(7)
    db.add_user(User("Julie", 17, "julie@gmail.com"))
    # db.update_user(3)
    db.show_info()
    users = db.search_users_by_name("Alex")
    users2 = db.search_users_by_age(18)
    users3 = db.search_users_by_email("iss")

    print("\nUsers with certain name: ")
    for user in users:
        user.show_info()

    print("\nUsers with certain age: ")
    for user in users2:
        user.show_info()

    print("\nUsers with certain email: ")
    for user in users3:
        user.show_info()

    db.remove_user(1)
    db.remove_user(3)
    db.remove_user(5)
    db.remove_user(7)
    db.remove_user(9)
    db.remove_user(11)

    print("\nUsers: ")
    db.show_info()

        