# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1

        dummy = temp = ListNode()
        rem = 0
        while l1 or l2:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            val = v1 + v2 + rem
            stub = val % 10
            rem = (val - stub) // 10
            temp.next = ListNode(stub)
            temp = temp.next
        
        while rem:
            stub = rem % 10
            rem = (rem - stub) // 10
            temp.next = ListNode(stub)
            temp = temp.next

        return dummy.next

            

        #then keep adding rem to either l1 or l2
        #then keep adding rem

        return dummy.next