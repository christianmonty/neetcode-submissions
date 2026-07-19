class Solution:
    def isValid(self, s: str) -> bool:
        Stack = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                Stack.append(i)
            else:
                if not Stack:
                    return False;
                item = Stack.pop()
                if item == '(' and i != ')' or item == '[' and i != ']' or item == '{' and i != '}':
                    return False
        if Stack:
            return False
        return True