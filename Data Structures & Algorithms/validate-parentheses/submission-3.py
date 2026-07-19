class Solution:
    def isValid(self, s: str) -> bool:

        stack = [] # any special functions to use?

        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if not stack:
                    return False
                if stack[-1] == '(' and c != ')' or stack[-1] == '[' and c != ']' or stack[-1] == '{' and c != '}':
                    return False
                else:
                    stack.pop()
        if not stack: return True
        return False
