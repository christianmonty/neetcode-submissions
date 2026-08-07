import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        # why don't we add tasks to min heapq as become available to process
        # then ranks on smallest index
        # have to maintain a global time to keep increasing
        # no premption, so once start processing it keeps going until finished
        # and yes I guess must sort by enqueue time so have original list (oh destroys index...)
        # maybe we add a hashmap where we hash the processing time? eh lot of space
        # need tuple of (processing time, index)
        # time = oldtime + processing time
        # if next min start time is >, bump time to that time
        # we want to sort tasks initially by start time (first index)
        # tricky about interaction of time increasing (add to pq) and process pq?
        
        for ind, val in enumerate(tasks):
            tasks[ind].append(ind) # now it's enqueue, process, index

        stasks = sorted(tasks) # should sort on first, need any ==?
        time = stasks[0][0] # first enqueue time
        index = 0 # remove endtime as a concept now
        outlist = []

        pq = []
        heapq.heapify(pq) # how we measure tasks in queue

        while True: # core processing in time, then while index is less
            while index < len(stasks) and stasks[index][0] <= time: # must consider anything within
                heapq.heappush(pq, (stasks[index][1], stasks[index][2])) # process time, index
                # invariant here is the time has already passed, we're catching up on tasks
                index += 1
            if index == len(stasks):
                break
            
            # now the pq has everything possible to enqueue
            if pq:
                nexttask = heapq.heappop(pq)
                outlist.append(nexttask[1])

                # time must advance by processing time now
                time += nexttask[0]
            else:
                # when time is so low for next enqueue, pq is empty
                time = stasks[index][0] # fast forward

        while pq:
            nexttask = heapq.heappop(pq)
            outlist.append(nexttask[1])

        return outlist






