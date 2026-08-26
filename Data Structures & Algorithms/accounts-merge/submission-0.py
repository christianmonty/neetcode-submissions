from collections import defaultdict, deque

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        # new idea, this is about connectivity but I can't figure out BFS/DFS cleanly here
        # so we'll use two hashmaps, one email -> indices, next indices -> identical indices
        # and then process each index, mark visited and then merge ones accordingly into single list
        # then sort and return those final lists

        # wait a cleaner way is first make hashmap email -> indices
        # then iterate over indices in accounts, and start a new queue, while queue not empty add indices to queue
        # pop index off queue, then process emails within and add indices for those emails to queue
        # then we have a list which is the indices as a connected component
        # once queue empty, add component to list of components
        # then do the merge and return list of merged emails


        hm = defaultdict(set) # this stores email -> indices of accounts
        for index, value in enumerate(accounts): # for each account
            for i, v in enumerate(value): # for each email in account
                if i > 0:
                    hm[v].add(index)

        visited = set() # visited indices of accounts
        queue = deque() # for current connected component
        component = [] # indices in component, MAYBE MAKE A SET
        component.append(0)
        arrangelist = []
        index = 0


        while index < len(accounts):
            if index not in visited: # juwt to cover all bases
                queue.append(index)
                while queue:
                    accountid = queue.pop()
                    for i, email in enumerate(accounts[accountid]):
                        if i > 0:
                            for indices in hm[email]:
                                if indices not in visited:
                                    component.append(indices)
                                    queue.append(indices)
                                    visited.add(indices)
                # now queue must be done, full connected component found
                arrangelist.append(component) # list of indices associated together
                component = [] # reset for new connected component
            index += 1
        
        outlist = []
        for sublist in arrangelist:
            accountname = accounts[sublist[0]][0] # first item at particular index in accounts, the name
            temp = set()
            for index in sublist:
                for i, val in enumerate(accounts[index]):
                    if i > 0 and val not in temp:
                        temp.add(val) # to remove duplicated
            sortlist = []
            for v in temp:
                sortlist.append(v)
            sortlist.sort()
            sortlist.insert(0, accountname)
            outlist.append(sortlist)
        return outlist





        # one idea of what we can do is the following
        # for each account, for j > 0 make hm entry and list of indices of the name (since can't use name itself since not unique)
        # then we've isolated from index of each email, which indices should be merged
        # but then by what mechanism do we unravel back the many to one relationship to merge?
        # really brute force way is you go through all the names, if you have another index and that's not in visited set, you add that onto current index (and add emails in the queue)
        # if email not yet processed, keep it and process it's duplicates emails too
        # otherwise skip if already processed. Then when exhausted a row, sort it's emails
        # then move onto the next unvisted index in original array

        # TBD if this solves it, then TBD if it solves it efficiently...

        # so first we go through entire thing, ignore name hash[email] = [list of indices]
        # then what we do is go through again, and collect all for that list (since invariant is two accounts belong to same person if share common email to both accounts)
        # add everything collected to visited set, then have list of list of what to merge
        # sort the sublists and then return as name + sorted sublists remove duplicates
        # maybe an extra set to remove the duplicates
        # conceptual way this turns into graph problem is 1 email maps to multiple indices.
        # for a given hm -> list of indices, if none have outindex, start a new one. Else, add any outindices you find to a queue to merge them?
        

        # HAVE TO TRY THIS PROBLEM W/PROPER BFS/DFS GRAPH SOLUTION
        '''
        visited = set() # to track indices already covered & added in
        # going to see if it works to mutate as we are reviewing, maybe we add to queue!
        # once queue is empty, then go to next nonvisited index!
        # wait another idea, if you want 1, 2, 6, 9 in a row and later 11, hash all those to first index, then hash other numbers where none of the values in index to next index
        for index, value in enumerate(accounts):
            q = deque()
            for i, v in enumerate(value):
                # visited.add(index) # tbd where to place
                if i > 0:
                    # TBD
                    for otherindex in hm[v]:
                        if otherindex not in visited:
                            q.add(otherindex)
        '''


            

        