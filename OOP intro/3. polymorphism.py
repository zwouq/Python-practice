class Dog:
    def sound(self):
        return "Woof!"

class Cat:
    def sound(self):
        return "Meow!"

class Cow:
    def sound(self):
        return "Muu!"

def make_sound(animal):
    print(animal.sound())

dog = Dog()
cat = Cat()
cow = Cow()

make_sound(dog)  # выводит: Woof!
make_sound(cat)  # выводит: Meow!
make_sound(cow)  # выводит: Muu!
