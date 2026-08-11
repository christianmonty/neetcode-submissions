class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        # ways of thinking about this...
        # move l and r until cross over
        # if left and right check, take left if <= match else right
        # while count is not filled
        # can copy array and subtract from each but extra space
        
        # 1. first find closest it's find the min if substract k from each
        # 2. then move left and right outwards until array is full
        # 3. then copy over that sorted window to output
        # 4. could also do as a PQ but this problem is for sliding window specifically

        closeindex = i = 0
        mindis = abs(arr[closeindex] - x)

        # what if there is more than 1 mindis?
        while i < len(arr):
            temp = abs(arr[i] - x)
            if temp < mindis:
                mindis = temp
                closeindex = i

            i += 1
        
        l = max(closeindex - 1, 0)
        r = min(closeindex + 1, len(arr) - 1)

        while r - l < k + 1:

            if l < 0:
                r += 1
            elif r > len(arr) - 1:
                l -= 1
            else:
                ldis = abs(arr[l] - x)
                rdis = abs(arr[r] - x)
                if ldis <= rdis:
                    l -= 1
                else:
                    r += 1
        
        outlist = []
        t = l + 1
        while t < r:
            outlist.append(arr[t])
            t += 1
        return outlist




        