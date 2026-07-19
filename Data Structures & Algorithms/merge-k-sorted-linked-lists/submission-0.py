# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class NodeWrapper:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other): # is this comparator
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        myheap = [] # never forget this
        dummy = ListNode(0)
        temp = dummy

        for l in lists:
            if l is not None:
                heapq.heappush(myheap, NodeWrapper(l))
        
        while myheap:
            nodewrapper = heapq.heappop(myheap)
            temp.next = nodewrapper.node
            temp = temp.next
            
            if nodewrapper.node.next:
                heapq.heappush(myheap, NodeWrapper(nodewrapper.node.next))
            
        return dummy.next