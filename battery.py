from abc import ABC, abstractmethod
from datetime import datetime

class Battery(ABC):

    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    @abstractmethod
    def needs_service(self):
        pass


class SpindlerBattery(Battery):
    def __init__(self, last_service_date):
        super().__init__(last_service_date)

    def needs_service(self):
        service_year = self.last_service_date.year + 2
        service_threshold_date = self.last_service_date.replace(service_year)
        return service_threshold_date < self.current_date

class NubbinBattery(Battery):
    def __init__(self, last_service_date):
        super().__init__(last_service_date)

    def needs_service(self):
        service_year = self.last_service_date.year + 4
        service_threshold_date = self.last_service_date.replace(service_year)
        return service_threshold_date < self.current_d

