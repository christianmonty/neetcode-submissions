class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalsum = 0
        hm = {}
        def remhm(val: int):
            if hm[val] == 1:
                hm.pop(val)
            else:
                hm[val] -= 1

        def addhm(val: int):
            if val not in hm:
                hm[val] = 1
            else:
                hm[val] += 1

        for n in nums:
            totalsum += n
            addhm(n)
        if totalsum % 2 == 1:
            return False
        halfsum = totalsum // 2
        

        def checkhm(half: int) -> bool:
            if half in hm:
                remhm(half)
                return True

            for i in range(1, half//2 + 1):
                rest = half - i
                if i in hm:
                    remhm(i)
                    if rest in hm:
                        remhm(rest)
                        return True
                    if checkhm(rest):
                        return True
                    addhm(i)
                elif checkhm(i):
                    if rest in hm:
                        remhm(rest)
                        return True
                    if checkhm(rest):
                        return True
            return False

        return checkhm(halfsum)
        
        