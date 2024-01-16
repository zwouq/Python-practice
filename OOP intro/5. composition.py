class Engine:
    def __init__(self, type):
        self.type = type

class GearBox:
    def __init__(self, type):
        self.type = type

class Car:
    def __init__(self, engine, gearbox):
        self.engine = engine
        self.gearbox = gearbox

engine = Engine("Diesel")
gearbox = GearBox("Auto")
car = Car(engine, gearbox)

print(car.engine.type)  # выводит: Diesel
print(car.gearbox.type)  # выводит: Auto