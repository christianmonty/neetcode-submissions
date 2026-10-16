class StoreItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        # pass  # Add: name, price


chips = StoreItem("Chips", 1.99) # Don't modify this line

# TODO: Access the attributes of the chips object and display them
# print(f"Item: [{chips.name}] - Price: $[{chips.price}]")
print(f"{chips.name}")
print(f"{chips.price}")



