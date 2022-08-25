class Car():
    def __init__(self, battery, engine):
        self.battery = battery
        self.engine = engine

    def needs_service(self):
        return self.battery.needs_service() or self.engine.needs_service()
