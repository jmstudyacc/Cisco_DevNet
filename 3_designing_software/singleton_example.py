"""
Singleton patterns are useful as they enable global access to an object, without creating a global variable.

Globals may seem a neat way to resolve the issue, but they run the significant threat of being overridden.
Other content may be erroneously stored in the GLOBAL variable causing unknown amounts of damage. The Singleton
pattern provides similar capability but protects the object from being overwritten.

This protection comes in the form:

- Making the class constructor private
- Creation of static method that returns the original instance to the caller

Class DataAccess() can only be instantiated once. The __init__() constructor first checks if an object instance
already exists and if it does an error is raised. If there is a requirement to access the object it should retrive
the instance by using get_instance()
"""


class DataAccess:
    __instance = None

    @staticmethod
    def get_instance():  # this line defines the client access method
        if DataAccess.__instance is None:
            DataAccess()
        return DataAccess.__instance

    def __init__(self):
        if DataAccess.__instance is not None:  # this line is used in preventing new object creation
            raise Exception("Instance exists")
        else:
            DataAccess.__instance = self
