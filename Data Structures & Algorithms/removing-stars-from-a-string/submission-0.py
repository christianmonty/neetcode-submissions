class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for c in s:
            if c == '*':
                stack.pop()
            else:
                stack.append(c)

        outstring = ""
        while stack:
            outstring = stack.pop() + outstring
        return outstring
