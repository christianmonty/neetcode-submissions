import heapq 

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        # given a list of lists, each inner list, (# pas, from, to) and a fixed seating capacity of the car
        # return true if can transport all passengers or false if not
        # must drive east, so MUST start with closest froms first, then sorted on second item

        # the key thing is comparing what's on top of pq with currently packed car
        # if what's on top of pq has start time < any end_time current car, then if top pas += cur pas < capacity, return false
        # else, add to current list of passengers (make room)
        # if top of pq start time >= "earliest ending", then pop off any that will have ended, add earliest
        # O(capacity) when add new one, O(len(trips)) for each trip off pq

        pq = []
        for t in trips:
            pq.append((t[1], t[2], t[0]))
        
        heapq.heapify(pq)
        # new order: (beg, end, seats)

        riders = []
        seats = 0
        
        while pq:
            top = heapq.heappop(pq)
            if not riders:
                if top[2] + seats <= capacity:
                    riders.append(top)
                    seats += top[2]
                else:
                    return False
            else:
                # if we are after firstend, might as well pop off some items to keep leaner
                riders = [r for r in riders if top[0] < r[1]]
                seats = 0
                for r in riders: # think of clean way to delete them here in place
                    seats += r[2]
                if top[2] + seats <= capacity: # if spare capacity, end now
                    riders.append(top)
                    seats += top[2]
                else:
                    return False

        return True

'''
            # cases:
            1. No riders, add if top[2] < capacity
            2. Full riders, add if top[0] > firstend, pop off endings then add
            3. Some riders, add if capacity allows, else return False
            4. Should order be check: capacity, then if > than firstend, or if > firstend (greedy) then if not if capacity.
'''
