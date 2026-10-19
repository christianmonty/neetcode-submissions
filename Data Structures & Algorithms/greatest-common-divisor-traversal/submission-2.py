class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        # one way of solving this is precalculating all the GCD's
        # so then we add to adjacency list, all pairs w/ gcd > 0.
        # ex. adj[0] = [2,...] for indices with gcd > 1
        # then we would add all those to a queue, and if we ever get to node looking for, return true if all
        # otherwise return false if q empty. We don't have to return the sequence of traversals

        adj = defaultdict(list)

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if math.gcd(nums[i], nums[j]) > 1:
                    adj[i].append(j)
                    adj[j].append(i)

        def checkseq(i: int, j: int) -> bool:
            q = deque()
            q.append(i)
            visited = set()
            visited.add(i)

            while q:
                node = q.popleft()
                # visited.add(node)

                for nxt in adj[node]:
                    if nxt not in visited:
                        q.append(nxt)
                        visited.add(nxt)
            return len(visited) == len(nums)
                    


        return checkseq(0, 1)
        

