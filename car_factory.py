from abc import ABC, abstractmethod
from car import Car
from battery import SpindlerBattery, NubbinBattery
from engine import CapuletEngine, WilloughbyEngine, SternmanEngine

class CarFactory(ABC):

    @abstractmethod
    def create_car(self):
        pass

class CalliopeFactory(CarFactory):
    def create_car(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        return Car(battery,engine)

class GlissadeFactory(CarFactory):
    def create_car(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        return Car(battery,engine)

class PalindromeFactory(CarFactory):
    def create_car(self, current_date, last_service_date, warning_light_on):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        return Car(battery,engine)

class RorschachFactory(CarFactory):
    def create_car(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        return Car(battery,engine)

class ThovexFactory(CarFactory):
    def create_car(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        return Car(battery,engine)