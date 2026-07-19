class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        # recall for pure Stack can just use a list, but for queue do from collections import deque
        # smaller one means abs not just neg less than positive

        # WAIT I missed that left and right are different directions, need to retry
        
        stack = []

        # then if top of stack moving left, and you are moving right just add it. Else do compare
        # if top of stack is moving right, and you are moving right just add it. Else do compare
        

        for a in asteroids:
            if not stack:
                stack.append(a)
            else:
                if a < 0:
                    while stack and stack[-1] > 0:
                        top = stack[-1]
                        if abs(top) == abs(a):
                            stack.pop()
                            a = 0
                            break
                        elif abs(a) > abs(top):
                            stack.pop()
                        else: # top is bigger
                            a = 0
                            break
                    if a:
                        stack.append(a)
                        # if destroy a, break out of the loop
                else:
                    stack.append(a)
        return stack