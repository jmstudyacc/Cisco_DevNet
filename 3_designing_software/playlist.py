
# the SELF argument in Python classes refers to the current object instance that you are working on
# it can be used to access the methods and state of that instance

class Playlist:
    def __init__(self):
        self.tracklist = []
        self._observers_list = []

    # implementing the logic required to add a track to the playlist, this is state information
    def add_track(self, track):
        self.tracklist.append(track)
        self._notify()      # this calls the private class method notify()

    # this private method traverse the observers list and updates each observer using the update() method
    def _notify(self):
        for observer in self._observers_list:
            observer.update(self)       # the observable object is passed as an argument

    # this method is used to return the current state of the program, it is used to sync up observer state
    def get_state(self):
        return self.tracklist

    # observers can subscribe to the publisher by appending them to the observers list using this attach() method
    def attach(self, observer):
        self._observers_list.append(observer)

    def remove(self, observer):
        self._observers_list.remove(observer)


class Jazz(Playlist):
    pass


class Funk(Playlist):
    pass


class Rock(Playlist):
    pass
