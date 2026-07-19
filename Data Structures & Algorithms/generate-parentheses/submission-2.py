class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        hs = set()

        def recurse(num: int, s: str):
            if not num:
                if isvalid(s):
                    hs.add(s)
                return
            recurse(num-1, s + '(')
            recurse(num-1, s + ')')
            return
        
        def isvalid(s: str) -> bool:
            c = s
            stack = []
            for char in c:
                if char == ')':
                    if not stack or stack[-1] != '(':
                        return False
                    stack.pop()
                else:
                    stack.append(char)
            return not stack

        recurse(2*n, "")
        outlist = []
        for val in hs:
            outlist.append(val)
        return outlist

        """
        def recurse(n: int) -> List[str]:
            if n == 0:
                return [""]
            reslist = recurse(n-1)
            reshalf = recurse(n//2)
            for r in reslist:
                hs.add("()" + r)
                hs.add(r + "()")
                hs.add("(" + r + ")")
            outlist = []
            while hs:
                s = hs.pop()
                outlist.append(s)
            return outlist


        return recurse(n)
        """
        