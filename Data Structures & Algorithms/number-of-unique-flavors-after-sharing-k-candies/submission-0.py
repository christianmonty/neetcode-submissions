class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        # ok so for each potential window of size k we need # of unique to left and to right of each
        # guess we can set up prefix and suffix sum of distinct flavors, but then ugh we must have set
        # so we just carry a set and add and remove stuff? Or hm so counts

        # sliding window question, keeping it as simple as possible

        # below keeps distinct flavors within block, but we need distinct outside of block....
        # first do past block, then add beginning and remove end as block shifts forward

        hm = {}
        e = k
        while e < len(candies):
            flavor = candies[e]
            if flavor not in hm:
                hm[flavor] = 1
            else:
                hm[flavor] += 1
            e += 1
        
        l = 0
        r = k # window size one greater
        maxc = len(hm.keys())

        while r < len(candies):
            # remove l and move it forward. Then add r and move it forward
            remove = candies[r]
            hm[remove] -= 1
            if hm[remove] == 0:
                del hm[remove]
            r += 1

            new = candies[l]
            if new not in hm:
                hm[new] = 1
            else:
                hm[new] += 1
            maxc = max(maxc, len(hm.keys()))
            l += 1

        return maxc



        '''

        hm = {}
        l = 0
        r = l + k - 1
        t = l
        maxc = 0
        while t < r:
            flavor = candies[t]
            if flavor in hm:
                hm[flavor] += 1
            else:
                hm[flavor] = 1
            t += 1
        maxc = len(hm.keys())

        while r < len(candies):
            flavor = candies[r]
            if flavor in hm:
                hm[flavor] += 1
            else:
                hm[flavor] = 1
            maxc = max(maxc, len(hm.keys()))

            remove = candies[l]
            hm[remove] -= 1
            if hm[remove] == 0:
                del hm[remove]

            l += 1
            r += 1


        return maxc

        '''


