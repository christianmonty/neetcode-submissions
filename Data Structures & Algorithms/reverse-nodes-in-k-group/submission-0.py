# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # one way of doing this, continue until reach end node
        # start, move forward k nodes as nextk (unless reach end)
        # then call reversek(head, k: int) -> reverse only k steps. Then go to end of that, and connect to nextk
        # then loop again starting with nextk as head

        # and separately return newHead for what to return from final function
        # this is conceptually kind of like 2 pointers + reverse a link list

        # remember the way we do this is while temp.next != null, recurse, then res -> next = self, self.next = null
        def reverse(temp: Optional[ListNode]) -> Optional[ListNode]:
            if not temp.next:
                return temp
            result = reverse(temp.next)
            result.next = temp
            temp.next = None
            return temp

        node = head
        newFront = None
        prevTail = None
        while node:
            i = 0
            first = node
            while i < k - 1:
                node = node.next
                i += 1
                if not node:
                    break
            if not node:
                break
            if not newFront:
                newFront = node
            nextk = node.next
            node.next = None
            newlast = reverse(first)
            newlast.next = nextk
            if prevTail: # didn't know to add this in here, missed this part
                prevTail.next = node
            prevTail = newlast # for next round, missed this part
            node = nextk
        
        return newFront or head # in case list < k


