class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        if not nums or len(nums) < 3:
            return []

        hm = {}
        for index, val in enumerate(nums):
            if val not in hm:
                hm[val] = [index]
            else:
                hm[val].append(index)

        i = 0
        outlist = []
        hs = set()
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                val = -(nums[i] + nums[j])
                if val in hm:
                    for index in hm[val]:
                        if index > i and index > j:
                            k = index
                            templist = [nums[i], nums[j], nums[k]]
                            templist.sort()
                            if tuple(templist) not in hs:
                                hs.add(tuple(templist))
                                outlist.append([nums[i], nums[j], nums[k]])
                            # tbd if need to hash this as tuple too
                j += 1
            i += 1

        return outlist

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        





        
        
        
        
        



        
        
        
        
    """
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

        """