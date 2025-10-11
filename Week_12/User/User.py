from abc import ABC, abstractmethod

class User(ABC):

    def __init__(self, username):
        self.username = username

    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def has_permissions(self, permission):
        pass