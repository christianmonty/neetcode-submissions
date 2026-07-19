# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        temp, count = head, 0
        while temp:
            count += 1
            temp = temp.next

        
        index = count - n
        temp, count = head, 0
        while temp:
            if index == 0:
                return temp.next
            if count == index - 1:
                if temp.next:
                    temp.next = temp.next.next
                else:
                    temp.next = None
                break
            temp = temp.next
            count += 1
        
        return head