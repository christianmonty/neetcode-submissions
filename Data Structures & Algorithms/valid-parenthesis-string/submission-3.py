class Solution:
    def checkValidString(self, s: str) -> bool:

        # so seems like stack add stuff, if right parenthesis pop, if left push, if star push
        # but then if star, maybe dp treating a 1. left, right or empty, and if any True return True

        outerstack = []
        memo = {} # hm instead of messy dp, need the stack states
        # what to do about if not stack
        # needed hint to realize this part

        def recurse(stack: Optional(List[str]), index: int) -> bool:
            if index >= len(s):
                if not stack:
                    return True # made it until end
                else:
                    return False
            key = (index, tuple(stack))
            if key in memo:
                return memo[key]
            c = s[index]

            if c == '(':
                stack.append(c)
                memo[key] = recurse(stack.copy(), index + 1)
            elif c == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                    memo[key] = recurse(stack.copy(), index + 1)
                else:
                    return False
            else:
                # try 3 recursions. If any return True, return True (as OR)
                skip = recurse(stack.copy(), index + 1)
                copied = stack.copy()
                if len(copied) > 0:
                    temp = copied.pop()
                    right = recurse(copied, index + 1)
                    copied.append(temp)
                else:
                    right = False
                copied.append('(')
                left = recurse(copied, index + 1)
                
                
                memo[key] = left or right or skip
            return memo[key]

        return recurse([], 0)