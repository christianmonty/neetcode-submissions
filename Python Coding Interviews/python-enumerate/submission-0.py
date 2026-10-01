from typing import List


def get_index_of_seven(nums: List[int]) -> int:
    
    for ind, val in enumerate(nums):
        if val == 7:
            return ind

    return -1


def get_dist_between_sevens(nums: List[int]) -> int:
    firstocr = secondocr = -1

    for ind, val in enumerate(nums):
        if val == 7 and firstocr == -1:
            firstocr = ind
        elif val == 7 and secondocr == -1:
            secondocr = ind
    
    return secondocr - firstocr


# do not modify below this line
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 8, 9]))
print(get_index_of_seven([2, 4, 7, 5, 7, 8, 4, 2]))

print(get_dist_between_sevens([1, 2, 7, 4, 5, 6, 7, 8, 9]))
print(get_dist_between_sevens([2, 7, 7, 7, 8]))
print(get_dist_between_sevens([7, 4, 8, 4, 2, 7]))
