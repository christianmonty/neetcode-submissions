class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        stack = []
        popind = 0

        for ind, val in enumerate(pushed):
            if val == popped[popind]:
                popind += 1
                while stack and popind < len(popped) and popped[popind] == stack[-1]:
                    stack.pop()
                    popind += 1

                '''
                while popind < len(popped) and stack:
                    nxt = stack[-1]
                    if nxt != popped[popind]:
                        return False
                    stack.pop()
                    popind += 1
                '''
            else:
                stack.append(val)

        while popind < len(popped) and stack:
            nxt = stack[-1]
            if nxt != popped[popind]:
                return False
            stack.pop()
            popind += 1

        return True
