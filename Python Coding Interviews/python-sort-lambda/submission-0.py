from typing import List

# rather than define a function separately just to pass into key of .sort() method is annoying
# instead we can define a function in a single line using a lambda function
# and from there pass directly into .sort() method

# format for lambda is: lambda thing: len(thing). Given a thing in an iterator as input, returns the length
# format is lambda input: do something to input
# lambda MUST be single EXPRESSION and can't contain multiple statements
# simple/convenient way to define simple functions w/o needing to define separate function...


def sort_words(words: List[str]) -> List[str]:
    words.sort(reverse=True, key=lambda w: len(w))
    return words


def sort_numbers(numbers: List[int]) -> List[int]:
    numbers.sort(key=lambda num: abs(num))
    return numbers


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
