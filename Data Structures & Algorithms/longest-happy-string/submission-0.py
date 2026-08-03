import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        # want max heap, do max one and twice if needed but then return to bottom?
        # if a, b or c are negative, then ignore
        pq = []
        res = ''
        last = ''
        tlast = ''
        pq.append((-a, 'a')) if a > 0 else None
        pq.append((-b, 'b')) if b > 0 else None
        pq.append((-c, 'c')) if c > 0 else None

        heapq.heapify(pq)

        # so we can add a mechanism to track last, and if last is same we try to choose another
        # don't think we necessarily need second last but we will see
        # ahhh I missed the 'at most' stipulation! can still stop safely earlier if possible!

        while pq:
            top = list(heapq.heappop(pq))
            if len(res) >= 2 and res[-1] == top[1] and res[-2] == top[1]:
                if not pq:
                    break # can have unused characters!
            
                temp = top
                top = list(heapq.heappop(pq))
                heapq.heappush(pq, tuple(temp))

            res += top[1] # ensure this is correct top here (scope)
            top[0] += 1
            
            if top[0]:
                heapq.heappush(pq,tuple(top))
            tlast = last
            last = top[1]

        return res
            


        