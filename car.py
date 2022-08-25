from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self):
        pass

class Calliope(Car):


class Glissade(Car):


class Palindrome(Car):



class Rorschach(Car):



class Thovex(Car):