# class is blueprint for creating objects
# build class name and then init method runs automatically when creating an object, initialize starting attributes
# self variable allow us add attributes to object directly (on initialization)

class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species




# Do not modify below this line
my_pet = Pet("Fluffy", "cat")
print(f"My pet is a {my_pet.species} named {my_pet.name}")
