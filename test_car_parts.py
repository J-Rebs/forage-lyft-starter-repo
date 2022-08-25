import unittest
from datetime import date
from car_factory import CarFactory
from engine import CapuletEngine, WilloughbyEngine, SternmanEngine
from battery import SpindlerBattery, NubbinBattery
from tire import Carrigan, Octoprime

# Updated tests to match solution, run in a single class but at the engine/battery level

class Tests(unittest.TestCase):
    def test_needs_service_true_capulet(self):
        current_mileage = 30001
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false_capulet(self):
        current_mileage = 30000
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

    def test_needs_service_true_sternman(self):
        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false_sternman(self):
        warning_light_is_on = False
        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.needs_service())
    
    def test_needs_service_true_willoughby(self):
        current_mileage = 60001
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false_willoughby(self):
        current_mileage = 60000
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

    def test_needs_service_true_Nubbin(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2016-01-25")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false_Nubbin(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2019-01-10")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())       

    def test_needs_service_true_Spindler(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2017-01-25")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false_Spindler(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2019-01-10")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())

    def test_needs_service_true_Carrigan(self):
        pressures = [0,0,0.9,0]
        tire = Carrigan(pressures)
        self.assertTrue(tire.needs_service())    

    def test_needs_service_false_Carrigan(self):
        pressures = [0,0,0.8,0]
        tire = Carrigan(pressures)
        self.assertFalse(tire.needs_service())    

    def test_needs_service_true_Octoprime(self):
        pressures = [1,0,1,1]
        tire = Octoprime(pressures)
        self.assertTrue(tire.needs_service())    

    def test_needs_service_false_Octoprime(self):
        pressures = [1,0,0,1]
        tire = Octoprime(pressures)
        self.assertFalse(tire.needs_service())    

if __name__ == '__main__':
    unittest.main()
