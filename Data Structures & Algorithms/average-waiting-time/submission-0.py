class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:

        # invariant is can carry forward last end time, we end at lastend + time[i]
        # total waittime = lastend + time[i] - arrival[i]
        # we could either append to that cell in customers OR make new array

        lastend = 0
        for index, val in enumerate(customers):
            ourend = max(lastend, val[0]) + val[1]
            ourtime = ourend - val[0]
            val.append(ourtime)
            lastend = ourend

        total = sum(val[2] for val in customers)
        return total / len(customers)


        