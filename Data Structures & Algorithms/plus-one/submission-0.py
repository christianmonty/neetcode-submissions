class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for d in digits:
            num = num * 10 + d
        num += 1
        string = str(num)
        outlist = []
        for c in string:
            outlist.append(int(c))
        return outlist