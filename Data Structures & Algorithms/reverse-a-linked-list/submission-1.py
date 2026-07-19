# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        curr = head
        after = curr.next
        curr.next = None

        while after != None:
            rest = after.next
            after.next = curr
            curr = after
            after = rest
        return curr
        
        
        """Attempt at recursive solution using helper function
        if not head:
            return head
        t = self.helper(head)
        t.next = None
        return head

    def helper(self, n: Optional[ListNode]):
        if n.next == None:
            return n
        head = self.helper(n.next)
        head.next = n
        return n 
        """