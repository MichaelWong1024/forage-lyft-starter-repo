
from datetime import date, timedelta

# Step 1: Creating the Serviceable Interface
class Serviceable:
    def needs_service(self) -> bool:
        raise NotImplementedError


# Step 2: Implementing Engine and Battery Classes
class Engine(Serviceable):
    pass

class CapuletEngine(Engine):
    def __init__(self, last_service_mileage: int, current_mileage: int):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self) -> bool:
        return (self.current_mileage - self.last_service_mileage) >= 30000


class Battery(Serviceable):
    pass

class SpindlerBattery(Battery):
    def __init__(self, last_service_date: date, current_date: date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        return (self.current_date - self.last_service_date).days >= 730


# Step 3: Implementing the Car Class
class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()


# Step 4: Implementing the CarFactory Class
class CarFactory:
    @staticmethod
    def create_car(engine: Engine, battery: Battery) -> Car:
        return Car(engine, battery)
