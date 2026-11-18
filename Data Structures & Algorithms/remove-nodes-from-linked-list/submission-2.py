# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import sys
sys.setrecursionlimit(10**6) # had to add this to pass final test case

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # so we can think of first pass going through to capture for each index? What comes later
        # as in a set
        # maybe return set recursively? so easy to check
        # wait we only need to return highest value to right when bouncing back left
        
        # if returned is > next, remove next

        if not head:
            return None

        head.next = self.removeNodes(head.next)
        if head.next and head.val < head.next.val:
            return head.next
        return head

        '''

        def recurse(node: Optional[ListNode]) -> int:
            if not node:
                return 0
            highest = recurse(node.next)

            if node.next and highest > node.next.val:
                node.next = node.next.next

            if node.val > highest:
                return node.val
            return highest

        newHead = ListNode()
        newHead.next = head
        recurse(newHead)

        return newHead.next
        '''
        