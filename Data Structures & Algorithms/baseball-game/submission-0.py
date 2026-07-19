from collections import deque

class Solution:

    def calPoints(self, operations: List[str]) -> int:

        stack = deque()

        for i in operations:
            
            if i == "+":
                newsum = stack[-1]  + stack[-2]
                stack.append(newsum)
                # TBD
            elif i == "C":
                stack.pop()
                # TBD
            elif i == "D":
                double = 2 * stack[-1]
                stack.append(double)
                # TBD
            else:
                stack.append(int(i))

        score = 0
        while stack:
            score += stack.pop()

        return score

        