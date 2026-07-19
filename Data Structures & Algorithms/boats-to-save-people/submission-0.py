class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # notice how order does not matter. We may wany to sort or add values to hash map
        # basically the two pointers is to pair off sorted order < weight limit

        count = 0
        first, last = 0, len(people) - 1
        sortp = sorted(people, reverse=True)

        while first < len(people) - 1 and sortp[first] >= limit:
            count += 1
            first += 1
        
        # now first points to heaviest below the limit
        while first <= last:
            if first == last:
                count += 1
                first += 1
                last -= 1
            elif sortp[first] + sortp[last] <= limit:
                count += 1
                first += 1
                last -= 1
            else:
                count += 1
                first += 1
        
        return count