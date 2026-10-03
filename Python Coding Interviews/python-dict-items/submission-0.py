from typing import Dict, List, Tuple

# so this returns all keys, all values, or both as view object (can make list()) from a hashmap

def get_dict_items(age_dict: Dict[str, int]) -> List[Tuple[str, int]]:
    return list(age_dict.items())


# do not modify below this line
print(get_dict_items({'Alice': 25, 'Bob': 30, 'Charlie': 35}))
print(get_dict_items({'Alice': 25, 'Bob': 30, 'Charlie': 35, 'David': 40}))
print(get_dict_items({'Bob': 30, 'David': 40, 'Charlie': 35, 'Alice': 25, 'Eve': 45}))
print(get_dict_items({'Alice': 25, 'Bob': 30, 'Charlie': 35, 'David': 40, 'Eve': 45, 'Frank': 50}))
