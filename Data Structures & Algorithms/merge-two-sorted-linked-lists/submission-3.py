# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

        
        """
        if not list1 and not list2:
            return list1
        elif not list1:
            return list2
        elif not list2:
            return list1
        newHead = list1
        if list1.val <= list2.val:
            newHead = list1
        else:
            newHead = list2
        
        while list1.next != None and list2.next != None:
            n1 = list1.next
            n2 = list2.next

            if list1.next.val >= list2.val and list1.val <= list2.val:
                list1.next = list2
                list2.next = n1
                list2 = n2
                list1 = list1.next
            elif list2.next.val >= list1.val and list2.val <= list1.val:
                list2.next = list1
                list1.next = n2
                list1 = n1
                list2 = list2.next
            elif list1.val >= n2.val:
                list2 = n2
            else:
                list1 = n1
        if list1.next == None:
            while list2 != None and list2.next != None:
                n2 = list2.next
                if list2.val <= list1.val and list1.val <= list2.next.val:
                    list2.next = list1
                    list1.next = n2
                    list1 = None
                    break
                elif list1.val <= list2.val:
                    list1.next = list2
                    break
                list2 = list2.next
        elif list2.next == None:
            while list1 != None and list1.next != None:
                n1 = list1.next
                if list1.val <= list2.val and list2.val <= list1.next.val:
                    list1.next = list2
                    list2.next = n1
                    list2 = None
                    break
                elif list2.val <= list1.val:
                    list2.next = list1
                    break
                list1 = list1.next
        if list1 != None and list1.next == None and list2 != None and list2.next == None:
            if list1.val <= list2.val:
                list1.next = list2
            else:
                list2.next = list1
            """
        return newHead
