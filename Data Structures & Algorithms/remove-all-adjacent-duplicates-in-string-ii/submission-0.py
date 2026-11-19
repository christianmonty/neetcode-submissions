class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        # one idea is two stacks, put onto 1 stack. Then move from one stack to next..
        # and when find three in a row, on the third, pop the second stack twice
        # then reset and keep going?
        # another idea, add to stack top [letter, count], and if same as stack top, count += 1
        # if top of stack then == k, pop that many from stack. Then keep adding
        # if len(begStack) same as len(endStack), stop since we're done

        stack = []

        # while True:
            # startStack = len(stack)

        for c in s:
            if stack and c == stack[-1][0]:
                stack.append([c, stack[-1][1] + 1])
            else:
                stack.append([c, 1])
            if stack and stack[-1][1] == k:
                for _ in range(k):
                    stack.pop()

        outstring = ""
        for c, count in stack:
            outstring += c
        
        return outstring
            # endStack = len(stack)
            # if startStack == endStack:
            #    break