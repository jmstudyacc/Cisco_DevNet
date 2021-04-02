# Python's implementation of classes & OOP

from toolbox import generate_device_name, is_ipv4_address


class Interface:
    def __init__(self, name, address):
        self.name = name
        self._address = address
        self.state = "Down"

    @property  # using properties in Python allows you to define input & output restrictions
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        if not is_ipv4_address(value):
            raise ValueError(f">> {value} is not a valid IPv4 address")
        self._address = value

    def __repr__(self):     # referred to as a Python magic method that defines object printout behaviour
        return str(vars(self))


"""
If you want to do anything with an object's data then you need to use dot syntax.
E.g.

>>> print(dev.hostname)     # this would print the hostname assigned to the dev Device object
>>> dev.motd = "No CLI allowed"     # this would ASSIGN the string after the assignment operator to motd of Device dev

"""


class Device:
    # constructor implemented below with some additional data included
    def __init__(self, hostname):
        self.hostname = hostname  # self.hostname is assigned to the variable hostname
        self.motd = None
        self.interface = None

    # functions in classes are methods - they must refer to self in python in their signature
    def show(self, p=None):
        # if the attribute is present, but not configured, return p which is None
        if not p:
            return str(vars(self))
        # if the object has that attribute configured, return the value of that attribute
        elif hasattr(self, p):
            return getattr(self, p)
        # if the object DOES NOT have the attribute at all, return the below message
        else:
            return f">> no attribute '{p}'"


# the Router class inherits the state & methods from the Device class, so you include Device in the parentheses
class Router(Device):
    pass


# you can assign a variable to the class but this doesn't seem to do a lot?
class DeviceX:
    # you have to call the init method, to assign a variable to the class instance e.g. dev1 = DeviceX()
    def __init__(self):  # as you know this method is a constructor for the class
        print('Device object created!')
