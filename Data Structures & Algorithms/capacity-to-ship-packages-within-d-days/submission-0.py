class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        # intuitively this feels similar to Koko's bananas
        # meaning we look at array from max(weights) as min if all own day to sum(weights) if all in a single day?
        # if days > len(weights), then if we do one package per day, least weight capacity is max(weights)
        
        maxw = max(weights) # linear search
        total = sum(weights)

        def checkWork(capac: int) -> bool:
            countd = 0
            temp = 0
            for w in weights:
                if temp + w <= capac:
                    temp += w
                else:
                    countd += 1
                    temp = w
            # for final day usage
            if temp > 0:
                countd += 1
                temp = 0
            return countd <= days


        l, r = maxw, total
        while l < r:
            mid = (l+r) // 2
            # test mid. If works, try left
            result = checkWork(mid)

            if result:
                r = mid
            else:
                l = mid + 1
        
        return r

        