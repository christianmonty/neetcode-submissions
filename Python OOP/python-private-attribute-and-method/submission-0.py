class PasswordManager:
    def __init__(self, password: str):
        self.__password = password
        pass  
    
    def verify_password(self, inputpass: str) -> bool:
        return self.__password == inputpass
    
    # TODO: Implement the verify_password method




# Don't modify the code below this line
my_password = PasswordManager("secret123")
print(my_password.verify_password("secret123"))  # Should print: True
print(my_password.verify_password("wrong"))      # Should print: False

# Unlike protected attributes which are accessible from child classes, private attributes are not!!