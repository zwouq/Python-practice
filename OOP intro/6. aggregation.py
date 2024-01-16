class Address:
    def __init__(self, street, city):
        self.street = street
        self.city = city

class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

address = Address("1234 Main St", "Springfield")
person = Person("John Doe", address)
person2 = Person("Mary Jane", address)

print(person2.address.city)  # выводит: Springfield
print(person2.name)  # выводит: Mary Jane
print(person2.address.street)  # выводит: 1234 Main St