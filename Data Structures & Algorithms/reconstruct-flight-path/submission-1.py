from collections import defaultdict
import heapq

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        

        # this seems like Djkstra's just with lexical order for cost vs. a weight value
        # Djkstra's means priority queue, sort by (destination, origin). Am I forgetting any other data structures?
        # so start with JFK, look in adjacency list then add new ones to pq
        # what does "valid" mean? each ticket used exactly once is interesting
        # since airports can be visited multiple times, how should we account for that? maybe deleting from hm after we add to pq. Well at end the # of hops must be == len(tickets)
        # ok wait this isn't Djkstra's since we aren't looking for smallest path across cut
        # my intuition to use pq for vals at each index of adj is correct, we can just O(nlogn) sort first
        # and then DFS I saw from hint but hadn't realized, though that makes sense to do...

        # ok I've never heard of Hierholzer's Iterative Algorithm...


        adj = defaultdict(list)
        for src, dst in sorted(tickets)[::-1]: # so can pop backwards first
        # does this sort on [src, dst] on which src or dst?
            adj[src].append(dst)

        res = []

        def recurse(src: str):
            while adj[src]:
                dst = adj[src].pop() # keep taking destinations off
                recurse(dst)
            res.append(src)

        recurse("JFK")
        return res[::-1] # return reversed since JFK added last


        '''
        # this was earlier DFS based approach from Solutions that timed out
            if len(res) == len(tickets) + 1:
                return True # includes JFK
            if src not in adj:
                return False

            temp = list(adj[src]) # possible next paths, why need to transform to list first?
            # hadn't thought to use backtracking here
            for i, v in enumerate(temp):
                adj[src].pop(i)
                res.append(v)
                if recurse(v): return True
                res.pop()
                adj[src].insert(i, v)
            return False
        '''
        



