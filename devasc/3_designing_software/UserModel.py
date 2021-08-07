"""
By using a language like UML, you should be able to construct the software in any language you need.
The ideas you are trying to achieve are held within the UML context. The UserModel code needs to be
independent of any other component in the MVC.

The following example will mimic a database storing user data.
"""

user_db = []


class User:
    # the selection of data here, is the definition of the object as per the Model - Model determines the object data
    def __init__(self, username, email):
        self.username = username
        self.email = email

    @staticmethod       # static methods are methods that do not require the object to be instantiated
    def get_user(user_id):
        for user in user_db:
            if int(user.id) == int(user_id):
                return user
        return False

    @staticmethod
    def get_users():
        return user_db

    # storage dependent implementation is not static, which is seen by the reference to self
    def store_user(self):
        user_id = len(user_db) + 1
        self.id = user_id
        user_db.append(self)
        return True

"""
In this instance, 2 values are set at object creation - username & email. This information is gained from the controller
via user input. There are 2 static methods, this is a class method that is a member of the class but not related to a
class instance directly, a static method can be called without instantiating the object.
"""