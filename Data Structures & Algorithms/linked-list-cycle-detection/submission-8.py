# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        cur = head
        after = cur.next
        while cur != after:
            if after == None or after.next == None:
                return False
            cur = cur.next
            after = after.next.next
        if cur == after:
            return True
        return False
#what to do about duplicate numbers?