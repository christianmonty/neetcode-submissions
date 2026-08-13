# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # brute force, for each set of adjacent pairs
        # pick smaller, try to divide large by smaller, then
        # since node.val <= 1000 try small - 1 all the way down
        # could do euclid's algorithm too for more efficient search

        # maybe we do a stock (gcd) function decomposed. could do math.gcd()
        # new array is size n-1 O(n) space
        # first calculate the GCD's, then populate into original list

        def gcd(a: int, b: int) -> int:
            # find gcd of (a,B) via Euclid's algorithm
            while b != 0:
                a, b = b, a % b
            return abs(a)

        temp = head
        while temp and temp.next:
            aNode = temp
            bNode = temp.next
            gcdval = gcd(aNode.val,bNode.val)
            aNode.next = ListNode(gcdval, bNode)
            temp = bNode
        
        
        return head


        