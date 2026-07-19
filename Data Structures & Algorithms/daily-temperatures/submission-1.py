class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        i = 0

        while i < len(temperatures):
            if not stack:
                stack.append(i)
                continue

            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                result[index] = i - index
            stack.append(i)
            i += 1

        return result



































        """
        size = len(temperatures)
        output = []
        if not temperatures:
            return output

        stack = []
        stack.append([temperatures[size-1], size-1])
        output.insert(0, 0)

        j = size - 2
        while j >= 0:
            while stack and temperatures[j] >= stack[-1][0]:
                stack.pop()
            if not stack:
                output.insert(0, 0)
            else:
                output.insert(0, stack[-1][1] - j)
            stack.append([temperatures[j], j])
            j -= 1
        
        return output
        """