# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # ok so regular linked list, to reverse we have next point to prev, prev point to next's next (iterative)

        # here what we'll do is 
        rightNode = leftNode = head
        rightcount = leftcount = 1
        newBeg = None
        while rightcount < right:
            rightNode = rightNode.next
            rightcount += 1
            if leftcount < left:
                newBeg = leftNode
                leftNode = leftNode.next
                leftcount += 1

        # now we have the sublist that we need to reverse
        newEnd = rightNode.next
        rightNode.next = None # to clear our list
        if newBeg:
            newBeg.next = None # to clear our list

        # perhaps we use 3 pointers to iterate this portion of list
        prev = leftNode
        cur = leftNode.next
        prev.next = newEnd

        # flow is, store cur's first next, then cur.next = prev, then cur = oldnext, prev = cur
        while cur:
            nextnxt = cur.next
            cur.next = prev
            ## issue with order here! must have prev and then cur!
            prev = cur
            cur = nextnxt


        if newBeg:
            newBeg.next = rightNode
            return head
        else:
            return rightNode
        

        