import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        maxProfit = [] # max heap
        minCapital = [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(minCapital) # turning it into a minHeap for capital

        j = 0
        while j < k:
            while minCapital and minCapital[0][0] <= w:
                _, p = heapq.heappop(minCapital)
                heapq.heappush(maxProfit, -p)
            
            if not maxProfit:
                break

            w += -heapq.heappop(maxProfit)

            j += 1

        return w


        '''

        # NOTE: this solution has a weird definition of capital, since it's NOT capital1 - capital2 + profit2,
        # it's capital1 + profit2, so capital is just a threshold, or is already burderned by capital cost...

        # couple things to notice here:
        # we could have a pq of profits, or of profit less capital
        # but we also need to account for starting capital, and may want a pq of capital too (minpq)
        # then we pop off profits, if don't have min cap then put back. If we do, then take?
        # or pop off delta (profit - capital), then rank by capital smallest to biggest
        # we also wouldn't want to take anything negative (capital > profits) even if we have k left
        # the greedy aspect is always take highest net (profit - capital) if have sufficient capital

        # one idea is we have tuple in pq of (-(profit - capital), capital, index)
        # so we can take smallest starting capital with best profit. index is for us to know what we picked but I guess that's uncessary, altho I think we should add to set( the indicies) just to keep track

        # ok wait if we put into pq, then pop all out (once), then we could iteratively start at beginning, take next remaining??
        # or does two pq's make it easier to not have to do over?
        pq = []

        for i in range(len(profits)):
            tup = (-(profits[i]), capital[i], i)
            heapq.heappush(pq, tup)

        j = 0
        capital = w
        # or stop early if max is lower...since at MOST k
        while j < k:
            temp = []
            while pq and pq[0][1] > capital:
                # pop and add to temp
                temp.append(heapq.heappop(pq))
            if pq:
                tup = heapq.heappop(pq)
                capital += -tup[0]
                # don't add index back. Guess don't need to add to set
            # then empty temp and put back
            while temp:
                heapq.heappush(pq, temp.pop())
            j += 1

        return capital

    '''
        