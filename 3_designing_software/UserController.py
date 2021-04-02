from abc import ABC, abstractmethod
import UserModel


class UserController(ABC):
    def __init__(self, view):
        self.view = view  # this controller is tied to a specific view

    @abstractmethod
    def create(self):
        raise NotImplementedError  # these methods need to be implemented by the strategy implementation

    @abstractmethod
    def get(self,id):
        raise NotImplementedError

"""
This class acts as an Abstraction interfaces & serves as the contract between the view 
and implementors of the controller. There may be many controllers for the view component but they must follow the 
UserController abstraction blueprint and implement these methods
"""


class SimpleController(UserController):
    def create(self, username, email):
        # this is validation of the user input, requests model and view update callbacks
        if '@' not in email:
            self.view.update_display(False, 'Email not valid')
        else:
            user = UserModel.User(username, email)
            result = user.store_user()
            if result:
                self.view.update_display(True, 'User created!')

    def get(self, id):
        user = UserModel.User.get_user(id)
        if user:
            self.view.update_display(True, user)
        else:
            self.view.update_display(False, f'User ID {id} not found')


"""
SimpleController is one of the strategies of the UserController interface. It implements the contract, but extends the
mandatory methods. The create() method reviews the user input & prevents user creation if the input is faulty. 

This shows how a controller can act as a mediator between the View and Model. If the input is accepted, then the data
is translated into a user object and the non-static method, store_user() is called on the object. This callback to 
UserModel kicks off the storing of the user in the database in the UserModel. If this is all successful, the 
controller reports the update to the view with update_display().

The get() method relies on the model static method get_user() to retrieve the user from the database. The controller
has no intelligence around the get() method, but simply calls the method and expects a positive or negative result. 

Tying it all together would be an application that would import the View module and call the create_user() method. 
Once a user is created you should also be able to get_user() with an ID. 

E.g.

from UserView import UserView
display = UserView()
display.create_user()...

display.create_user()...
display.get_user()...

"""