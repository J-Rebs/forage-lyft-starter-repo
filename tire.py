from abc import ABC, abstractmethod
from datetime import datetime

class Tire(ABC):

    def __init__(self, pressures):
        self.pressures = pressures

    @abstractmethod
    def needs_service(self):
        pass

class Carrigan(Tire):
    def __init__(self, pressures):
        super().__init__(pressures)
    
    def needs_service(self):
        for v in self.pressures:
            if v >= 0.9:
                return True
        return False

class Octoprime(Tire):
    def __init__(self, pressures):
        super().__init__(pressures)
    
    def needs_service(self):
        if sum(self.pressures) >= 3:
            return True
        else:
            return False
