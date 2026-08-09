class Solution:
    def decodeString(self, s: str) -> str:

        # things we have to do:
        # 1. strip out the int even if multiple digits, next int is AFTER closing bracket
        # 2. once we get to first closing bracket, we are done with recursion. We start repeating things
        # inside each set of brackets, then repeat inner brackets that # of times
        # 3. When you pop out the stack, copy that substack n # of times
        # # while there's a stack, keep going adding stuff see a closing bracket
        # if no stack, output directly

        outlist = []
        stack = []
        index = 0
        substring = ""
        # if stack empties, reset substring to 0

        while index < len(s):
            val = s[index]
            if val >= 'a' and val <= 'z' and not stack:
                outlist.append(val)
            else:
                if val == ']':
                    # pop stack until opening bracket, and repeat n # of times
                    while stack and stack[-1] != '[':
                        top = stack.pop()
                        # add to front of substring
                        substring = top + substring
                        # invariant is won't encounter a number before an open '['
                    # now we must be on the open '['
                    if stack:
                        stack.pop() # for the '['
                    if stack:
                        numcopies = stack.pop() # for the int
                    substring = substring * numcopies
                    if stack: # put back on
                        stack.append(substring)
                    else:
                        outlist.append(substring)
                    substring = ""
                elif val == '[':
                    stack.append(val)
                elif val >= 'a' and val <= 'z':
                    stack.append(val)
                else: # must be a number
                    num = ""
                    while index < len(s) and s[index] >= '0' and s[index] <= '9':
                        # add to some other data structure? or stack but convert to int
                        # keep adding numbers to string then we will convert to int
                        num += s[index]
                        index += 1
                    index -= 1 # have to move this pointer back, ALWAYS TRACE INDEX ON AN INPUT
                    # could error check here for index out of range
                    number = int(num)
                    stack.append(number)
                # if stack now empty, substring = ""
            index += 1
        return ''.join(outlist)

            






        # when you see a closing bracket, whatever was within bracket repeat that # of times
        # maybe instead of stragith stack we store tuple (num, string) so we know what to repeat
        # then we see another close bracket, pop until see open bracket and repeat the thing that many times
        # or maybe (open bracket, number) for # to repeat?

        # iterate across s. If letter and no stack, add to res. If int and then open bracket, pop onto stack
        # if there's stack, put everything next within.
        # if closing bracket, pop stack until open bracket and repeat that many times!
        
        # can we split on delimeter '[' and then int is stuff before? rest is processed separately
