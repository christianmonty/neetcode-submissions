class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        for n in nums:
            if n in dict1:
                dict1[n] = dict1[n] + 1
            else:
                dict1[n] = 1
        
        maxfreq = 0
        for key in dict1:
            if dict1[key] > maxfreq:
                maxfreq = dict1[key]

        topk = [[] for val in range(maxfreq+1)]
        for key in dict1:
            topk[dict1[key]].append(key)
        count = 0
        done = False
        output = []
        for item in reversed(topk):
            for thing in item:
                if count >= k:
                    done = True
                if not done:
                    output.append(thing)
                    count += 1
            if done:
                break
        return output


