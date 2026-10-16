class Account:
    def __init__(self, title, balance):
        self.title = title
        self._balance = balance
        pass
    
    def display_balance(self) -> None:
        print(f"Balance: ${self._balance}")
        pass


# Do not modify the code below this line
account = Account("John", 1000)
account.display_balance()

# Python doesn't officially enforce access control for protected attributes
# underscore prefix is convention to signal to other devs don't access attributes from the outside  
# to access protected attributes & methods use the public version of each