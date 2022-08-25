from abc import ABC, abstractmethod

from battery import SpindlerBattery, NubbinBattery
from engine import CapuletEngine, WilloughbyEngine, SternmanEngine

class Car(ABC):
    def __init__(self, battery, engine):
        if battery == 'Spindler':
            self.battery = SpindlerBattery
        elif battery == 'Nubbin':
            self.battery = NubbinBattery
        else:
            raise Exception("Invalid Battery Type")

        if engine == 'Capulet':
            self.engine = CapuletEngine
        elif engine == 'Willoughby':
            self.engine = WilloughbyEngine
        elif engine == 'Sternman':
            self.engine = SternmanEngine
        else:
            raise Exception("Invalid Engine Type")

    @abstractmethod
    def needs_service(self):
        return self.battery.needs_service() or self.engine.needs_service():

class Calliope(Car):
    def __init__(self, battery, engine):
        super().__init__(battery, engine)

    def needs_service(self):
        super().needs_service()


class Glissade(Car):
    def __init__(self, battery, engine):
        super().__init__(battery, engine)

    def needs_service(self):
        super().needs_service()

class Palindrome(Car):
    def __init__(self, battery, engine):
        super().__init__(battery, engine)

    def needs_service(self):
        super().needs_service()

class Rorschach(Car):
    def __init__(self, battery, engine):
        super().__init__(battery, engine)

    def needs_service(self):
        super().needs_service()

class Thovex(Car):
    def __init__(self, battery, engine):
        super().__init__(battery, engine)

    def needs_service(self):
        super().needs_service()