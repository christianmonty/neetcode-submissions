class Library:
    books_available = 100    # Total books in library. Class attribute

    # TODO: Implement class methods to manage book lending
    @classmethod
    def lend_books(cls, number):
        Library.books_available -= number

    # TODO: Implement return_books method to increase the number of books available
    @classmethod
    def return_books(cls, number):
        cls.books_available += number


# class method can work on entire class (thing) rather than individual instances. They don't have access to instance attributes
# cls is convention instead of self for class methods (vs. instance methods). And must do @classmethod

# Don't change the code below
print(f"Initial status: {Library.books_available} books available")
Library.lend_books(30)
print(f"After lending: {Library.books_available} books available")
Library.return_books(10)
print(f"After return: {Library.books_available} books available")
