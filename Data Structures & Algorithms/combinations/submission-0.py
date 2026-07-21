class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # here basically we need two tracks. Until count is == k, add yourself, take path, then remove yourself, take path
        # since n is small, we make array ahead of time
        intlist = [i for i in range(1, n+1)] # list comprehension

        outlist = []
        
        def backtrack(index: int, sublist: Optional[List[int]]):
            if len(sublist) == k: # list is too big
                outlist.append(sublist.copy())
                return
            if index == len(intlist):
                return
            
            sublist.append(intlist[index])
            backtrack(index+1, sublist)
            sublist.remove(intlist[index]) # get cleaner about popping this from for loop within vs. relying on unique element
            backtrack(index+1, sublist)

        backtrack(0, [])
        return outlist
        