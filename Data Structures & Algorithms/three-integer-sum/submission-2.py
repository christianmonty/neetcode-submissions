class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #first store HasmMap of every value and it's frequency
        hm = {}
        hs = set()
        for item in nums:
            if item in hm:
                hm[item] += 1
            else:
                hm[item] = 1
        #then take 2 pointers and iterate through all pairs, checking if sum is in HashMap (incl. duplicates)
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                sum = -(nums[i] + nums[j])
                res = []
                if sum in hm:
                    count = hm[sum]
                    if sum == nums[i] == nums[j] and count > 2:
                        res = [sum, sum, sum]    
                    elif sum == nums[i] and count > 1:
                        res = [sum, sum, nums[j]]
                    elif sum == nums[j] and count > 1:
                        res = [sum, sum, nums[i]]
                    elif sum != nums[i] and sum != nums[j]:
                        res = [sum, nums[i], nums[j]] 
                    if res == [0, 0, 0] and count < 3:
                        res = []
                    if res:
                        res.sort()
                        hs.add(tuple(res))
                j += 1
            i += 1
        
        answer = []
        for item in hs:
            answer.append(list(item))
        return answer