class SmartDevice:
    def __init__(self, name: str):
        self.name = name

# TODO: Implement the SmartLight class
class SmartLight(SmartDevice):
    def turn_on(self):
        print(f"{self.name} is turned on")


    def turn_off(self):
        print(f"{self.name} is turned off")



# Don't change the code below
device = SmartLight("Smart Light")
device.turn_on()
device.turn_off()

# inheritance allows child class to have some properties from base class, and extensions
# syntax for inheriting is class ChildClass(ParentClass):...
# when instance of child class is created, constructor of parent class is called automatially
# what if child class adds additional parameters what is order of intialized attributes
