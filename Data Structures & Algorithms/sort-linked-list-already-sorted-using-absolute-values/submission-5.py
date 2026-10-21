# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortLinkedList(self, head: ListNode) -> ListNode:

        # ok one idea is we split into two lists, remove negative nodes and keep adding to front of newlist
        # what we'd be left with is just the positive list sorted. Then we can have end of negative list point to beginning of positive list. And return beginning of negative list

        negFront = ListNode(-5001) # as sentinel node
        # every time new node, temp = negFront.next. negFront.next = newnode, newnode.next = temp
        fakeFront = ListNode() # defaults to 0
        fakeFront.next = head # this is cleaner way, vs. trying to account for a "Start" positive node
        node = fakeFront

        while node and node.next != None:
            nxt = node.next
            if nxt.val < 0:
                after = nxt.next
                temp = negFront.next
                negFront.next = nxt
                nxt.next = temp
                node.next = after
            else:
                node = node.next # otherwise keep processing next positive node. Missed this part

        lastNeg = negFront
        while lastNeg and lastNeg.next:
            lastNeg = lastNeg.next
        lastNeg.next = fakeFront.next

        return negFront.next
