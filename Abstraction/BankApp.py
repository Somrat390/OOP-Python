from abc import ABC,abstractmethod

class Bank(ABC):
    def database(self):
        print("Connected to Database")
    @abstractmethod
    def security(self):
        pass


