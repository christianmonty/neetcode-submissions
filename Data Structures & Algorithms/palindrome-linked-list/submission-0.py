# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        stack = []
        temp = head
        count = 0
        if head:
            count = 1
        while temp.next:
            temp = temp.next
            count += 1

        temp = head
        cnt = 0
        while temp:
            if cnt < count // 2:
                stack.append(temp.val)
            elif cnt > count // 2 or (cnt == count // 2 and count % 2 == 0):
                if stack.pop() != temp.val:
                    return False
            temp = temp.next
            cnt += 1

        return True