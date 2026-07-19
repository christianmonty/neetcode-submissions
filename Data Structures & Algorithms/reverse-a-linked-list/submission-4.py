# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # attempt here of reversing linked list in place
        newHead = head

        def reverse(temp: Optional[ListNode]) -> Optional[ListNode]:
            if not temp:
                return None
            if not temp.next:
                nonlocal newHead 
                newHead = temp        
                return temp

            prev = reverse(temp.next)
            if prev: prev.next = temp
            temp.next = None

            return temp
        
        reverse(head)
        return newHead




    '''
    if not head:
        return head

    newHead = head
    if head.next:
        newHead=self.reverseList(head.next)
        head.next.next = head
    head.next = None
    return newHead
    '''

    """
    def recurseList(root: Optional[ListNode]) -> Optional[ListNode]:
        if root.next is None:
            nonlocal head
            head = root
            return root
        prev = recurseList(root.next)
        prev.next = root
        root.next = None
        return root
    recurseList(head)
    return head
    """

    
    """
    if not head:
        return head
    curr = head
    after = curr.next
    curr.next = None

    while after != None:
        rest = after.next
        after.next = curr
        curr = after # don't mess up this ordering with following line!
        after = rest
    return curr
    
    
    #Attempt at recursive solution using helper function
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