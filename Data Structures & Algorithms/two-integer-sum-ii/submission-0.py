class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        outlist = []

        i, j = 0, len(numbers)-1

        while i < j:
            lres = target - numbers[i]
            rres = target - numbers[j]
            if lres == numbers[j]:
                outlist.append(i+1)
                outlist.append(j+1)
                return outlist
            if lres < numbers[j]:
                j -= 1
            elif rres > numbers[i]:
                i += 1




'''
        def binS(val: int, left: int, right: int) -> int:
            if left > right:
                return -1
            mid = (left + right)/2
            if numbers[mid] == val:
                return mid:
            if numbers[mid] > val:
                return binS(val, left, mid)
            else:
                return binS(val, mid+1, right)

'''
        