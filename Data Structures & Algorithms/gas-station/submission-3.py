class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        # clear to me that at each index, gas - cost is what matters we want to start positive
        # if total sum of cost is more than sum of gas, must return -1

        l = 0
        index = 0
        total = 0

        if sum(gas) < sum(cost):
            return -1

        while l < len(gas):
            total += gas[l] - cost[l]
            # tricky, this part was not intuitive for me
            if total < 0:
                total = 0
                index = l + 1
            l += 1

        return index
        