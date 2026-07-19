class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        # brute force way using extra space, have for each index (from, to) of trusting each other
        # will do this way first
        itrust = [0] * (n+1)
        trustme = [0] * (n+1) # for convenience
        for t in trust:
            itrust[t[0]] += 1
            trustme[t[1]] += 1

        for i in range(1, n+1):
            if itrust[i] == 0 and trustme[i] == n - 1:
                return i
        return -1


        # graphs way is build a graph, then pick a node. If trust no one, it's judge. O/w, DFS to find judge
        # provided edges, build the graph
        # wait but if no judge exists, then could get into a loop w this method
        

        