from abc import ABC, abstractmethod


class Device(ABC):
    def __int__(self, hostname):
        self.hostname = hostname

    @abstractmethod     # abstract method is defined by using a decorator
    def save_config(self):
        pass

    def __auditLog(self):   # use of underscores to semantically define private data & methods
        # logs user actions
        pass

    def action(self):
        # performs desired action & logs
        (self.__auditLog())


class Router(Device):   # parent abstract methods must be overwritten by the children
    def save_config(self):
        pass    # Router device specific implementation
