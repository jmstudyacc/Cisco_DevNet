import UserModel
from UserController import SimpleController


class UserView:
    def __init__(self):
        self.controller = SimpleController(self)  # registering a strategy, the controller implementation

    # controller triggered - displays update
    def update_display(self, state, msg):   # tightly coupled as it deserializes a user object, make it less dependent?
        if isinstance(msg, UserModel.User):
            msg = f'{msg.username};{msg.email}'
        print(f"{'Success' if state else 'Error'}>>>{msg}")

    def create_user(self):
        username = input('username: ')
        email = input('email: ')
        self.controller.create(username, email)

    def get_user(self):
        user_id = input('user id: ')
        self.controller.get(user_id)


"""
This code is responsible for taking in user input and printing it. It has a light dependency on the model due to the 
import statement. This view is simple, it is a CLI display application that takes the user input for Username and Email
and sends it to the controller for further processing. It is also has a display procedure to show a user with a 
specified User ID.

The View and Controller are loosely coupled thanks to how the data is shared. Instead of sending an object to the
controller the View sends the Controller a string. The update_display() method is used to update the view & 
represents the connection from the Controller to the View. 

When the Controller performs an action requested from the View, it calls back to the View to update the presentation. 
"""