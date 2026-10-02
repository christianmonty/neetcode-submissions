class Pet:
    def __init__(self, name: str):
        self.name = name
        self.hunger = 5

    def feed(self):
        # TODO: Implement this method
        # It should decrease the pet's hunger by 1
        # and print a message about feeding the pet
        self.hunger -= 1
        print(f'Fluffy has been fed.')
        print(f"Fluffy's hunger level: {self.hunger}")

# Create a pet
my_pet = Pet("Fluffy")

# TODO: Feed the pet three times
# methods belong to a class or object, they define BEHAVIOR of class or object, things it can do
# RECALL, class methods need a SELF!! so can be called outside it
my_pet.feed()
my_pet.feed()
my_pet.feed()