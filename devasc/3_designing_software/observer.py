from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self):       # update() method must be implemented by concrete observers and not just observers
        raise NotImplementedError


"""
The below class, User(Observer), is the concrete observer in this instance
It inherits the Observer class meaning that it must implement the update() method
This represents a user object that sores track references from all the genres to which the user is subscribing.

The track list will be updated when there is a change to one of the subscribed genre object & the publisher calls
the update() method of a user object. When this occurs the user objects are notified and the get_state() method on 
the publisher object that was passed is called.

The observer then updates its state with the state of the publisher
"""


class User(Observer):
    def __init__(self, username):
        self.username = username
        self.tracklist = []

    # this will fetch the state from the observable object that is passed to the method
    def update(self, publisher):
        print(f"> Updating user {self.username}")
        state = publisher.get_state()
        self.tracklist.append(state)

    def play_songs(self):
        print(f"Playing {self.tracklist} to {self.username}")