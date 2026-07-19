class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        hm = {i: [] for i in range(0, numCourses)}
        for idx, value in prerequisites:
            hm[idx].append(value)

        hs = set()

        def dfs(idx: val) -> bool:
            # base case: if node itself has no edges
            if len(hm[idx]) < 1:
                return True
            for val in hm[idx]:
                if val not in hs:
                    hs.add(val)
                    res = dfs(val)
                    if res:
                        hm[idx].remove(val)
                        hs.remove(val)
                    else:
                        return False
                else:
                    return False
            return True

        for idx in hm:
            res = dfs(idx)
            if not res: return False

        return True