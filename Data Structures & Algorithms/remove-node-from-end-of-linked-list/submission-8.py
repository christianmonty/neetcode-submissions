# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        count = 0
        fast = slow = head

        while count < n:
            fast = fast.next
            count += 1
        
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
            count += 1

        if not fast and count == n:
            head = slow.next
        elif slow.next:
            slow.next = slow.next.next
        
        return head

























        '''
        fast, slow = head, head
        count = 0
        while count < n:
            fast = fast.next
            count += 1

        if not fast:
            return slow.next

        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head
        '''
        """
        #below is an iterative solution
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
        """