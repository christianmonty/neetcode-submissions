from collections import Counter
from typing import Counter as CounterType

# we can use Counter as follows, call Counter(list) which then tracks count
# must import Counter from collections. Keys are list elements vals are # occurences
# counter.update(nums) to increase counts per another list of info


def count_chars(s1: str, s2: str) -> CounterType:
    counter = Counter(s1)
    counter.update(s2)
    return counter
  

# do not modify below this line
print(count_chars("hello", "world"))
print(count_chars("hello", "worldhello"))
print(count_chars("areallylongstring", "heyhowisitgoing"))
