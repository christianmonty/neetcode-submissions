class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def make_sound(self) -> None:
        print("Animal is making a sound")

class Dog(Animal):
    def make_sound(self) -> None:
        print(f"{self.name} says: Woof!")

class Cat(Animal):
    def make_sound(self) -> None:
        print(f"{self.name} says: Meow!")

def make_sound(animal: Animal):
    animal.make_sound()


# TODO: Create the Dog and Cat classes with make_sound method


# TODO: Create a common interface that takes any object of type Animal (or its subclasses) and calls their make_sound method


# power of polymorphism is that can take object of superclass or subclass, and behavior can differ. Powerful
# can give method instance of any of them. Achieved through method overloading in Python or duck typing (unrelated classes can both call the method) can use type (thing) and then thing.method() which will work if it has it


# Do not change the code below
animal = Animal("Rabbit")
animal.make_sound()

animal = Dog("Buddy")
animal.make_sound()

animal = Cat("Whiskers")
animal.make_sound()
