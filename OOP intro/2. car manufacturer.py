class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def print_details(self):
        print(f"Manufacturer: {self.make}")
        print(f"Model: {self.model}")

class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model) #is a built-in function in Python that is used to give access to the methods of a parent or sibling class. It is commonly used in class inheritance to call methods of a parent class without needing to name the parent class explicitly.
        self.year = year

    def print_details(self):
        super().print_details()
        print(f"Year: {self.year}")

car = Car("Toyota", "Camry", 2020)
car.print_details()
car2 = Car("Mercedes", "S600", 2023)
car2.print_details()