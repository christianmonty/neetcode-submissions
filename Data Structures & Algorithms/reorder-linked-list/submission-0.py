# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#wrong
import math

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        fast, slow, prev = head, head, head
        #use fast and flow pointers to find mid!
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        if fast:
            prev = slow
            slow = slow.next

        def reverseList(node: Optional[ListNode]) -> ListNode:
            if not node:
                return node
            newNode = node

            if node.next:
                newNode = reverseList(node.next)
                node.next.next = node
            node.next = None
            return newNode

        prev.next = None
        last = reverseList(slow)
        first = head

        while last and first:
            newlast = last.next
            last.next = first.next
            first.next = last
            first = last.next
            last = newlast



        """
        #Assuming no cycles lol
        n = 0
        temp = head
        hs = {}
        while temp:
            n += 1
            hs[n] = temp
            temp = temp.next
        count = n
        beg = head
        while count > (n // 2):
            temp = hs[count-1]
            begnext = beg.next
            beg.next = temp
            temp.next = begnext
            beg = temp.next
            count -= 1
        """