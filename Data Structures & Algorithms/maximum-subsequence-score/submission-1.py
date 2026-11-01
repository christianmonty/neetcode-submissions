import heapq

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:

        # ended up copying this solution since coulnd't pass all test cases

        pq = []
        pairs = sorted(zip(nums2, nums1), reverse=True)
        total = 0
        maxbest = 0

        for n2, n1 in pairs:
            heapq.heappush(pq, n1)
            total += n1

            if len(pq) > k:
                total -= heapq.heappop(pq)
            if len(pq) == k:
                maxbest = max(maxbest, total * n2)

        return maxbest




    '''
    # my original attempt here, I didn't realize need to sort nums2 in reverse most importantly and then pq is just nums1

    # thinking out loud, I guess could do prefix sum array for nums1 to quickly calculate totals
        # and then for nums2, we could do priority queue removing smallest len(nums2) - k, tho that may not be optimal...
        # oh and wait we need to pick fragmented indices so prefix sum is not ideal

        # super greedy approach is just get rid of smallest n - k indices in nums2, and multiply min by rest in nums1
        # one thing we can do is sum all all of nums1, add to pq (nums2[i], nums1[j]) and then subtract from total as we remove
        for i in range(len(nums1)):
            heapq.heappush(pq, (nums2[i] * nums1[i], nums2[i], nums1[i]))
            total += nums1[i]

        while len(pq) > k:
            subtotal, n2, n1 = heapq.heappop(pq)
            total -= n1

        minval = pq[0][1]
        while pq:
            _, temp, _ = heapq.heappop(pq)
            minval = min(minval, temp)

        return total * minval
    '''
