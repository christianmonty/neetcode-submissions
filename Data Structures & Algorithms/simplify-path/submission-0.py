class Solution:
    def simplifyPath(self, path: str) -> str:

        # this question is not my favorite since examples w "..." as a string seem to contradict the instructions 

        # if first slash missing, return error?
        # then capture next path char by char, if match a thing put in stack (continue pattern)
        # else discard the junk
        # then pop everything from the stack to fill path back to front?
        # reason we use a stack is because parent directory is like popping from the Stack

        res = []
        path = path + '/'
        name = ""
        stack = []

        for p in path:
            if p == '/':
                if name == "..":
                    if stack:
                        stack.pop()
                elif name and name != '.':
                    stack.append(name)
                name = ""
            else:
                name = name + p

        while stack:
            res.insert(0, '/' + stack.pop())

        if not res:
            return '/'
            
        
        return "".join(res)
