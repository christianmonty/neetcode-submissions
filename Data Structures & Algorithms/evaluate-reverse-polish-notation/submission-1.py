class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            resf = res1 = res2 = 0
            if t == '+' or t == '-' or t =='*' or t == '/':
                if stack:
                    res1 = stack.pop()
                    if stack:
                        res2 = stack.pop()
                if t == '+':
                    resf = res1 + res2
                elif t == '-':
                    resf = res2 - res1
                elif t == '*':
                    resf = res1 * res2
                else:
                    if res1 != 0:
                        resf = int(res2/res1)
                stack.append(resf)

            else:
                stack.append(int(t))
        return stack[-1]