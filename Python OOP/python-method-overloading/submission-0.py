class TextProcessor:
    # Implement method overloading for format_text method
    def format_text(self, text1: str, text2: str = ""):
        return text1 + text2 if text2 != "" else text1.upper()


# method overloading allows a class to have multiple methods w/same name, different parameters
# but we can't do this naturally in Python must use default arguments, c: int = 0
# or variable length arguments, *args: int... and then return sum(args)

# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
