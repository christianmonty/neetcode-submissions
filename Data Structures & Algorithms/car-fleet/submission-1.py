class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #idea is sort tuples by position
        #then start with end and put on stack. Move backwards and if (end-pos)/speed < top of stack (meaning the latest car would have passed)
        #then add to same fleet, if it's slower then it never would have caught up, pop entire stack and increment fleet count, put new on stack
        slist = []
        for i in range(len(position)):
            tup = (position[i], speed[i])
            slist.append(tup)
        
        slist.sort()
        stack = []
        count = 0
        j = len(slist) - 1

        while j >= 0:
            calc = (target - slist[j][0]) / slist[j][1]
            if not stack:
                stack.append(calc)
                count += 1
            elif calc > stack[-1]:
                while stack:
                    stack.pop()
                count += 1
                stack.append(calc)
            j -= 1

        return count
        