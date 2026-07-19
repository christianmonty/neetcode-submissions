class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        complist = [0] * len(nums)

        for i, val in enumerate(nums):
            hm[val] = i
            complist[i] = target - val

        outlist = []
        for i, val in enumerate(nums):
            if complist[i] in hm and hm[complist[i]] != i:
                outlist.append(i)
                outlist.append(hm[complist[i]])
                break

        return outlist


































        '''
        values = set()
        for i in nums:
            temp = target - i
            if temp in values:
                l1 = nums.index(i)
                l2 = nums.index(temp)
                if l2 < l1:
                    l3 = l1
                    l1 = l2
                    l2 = l3
                elif l2 == l1:
                    l2 = nums.index(i, l1 + 1)
                return [l1, l2]
            values.add(i)
            '''