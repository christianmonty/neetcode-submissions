"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        olist = []
        q = []

        node = head

        while node:
            olist.append(node)

            val = node.val
            newNode = Node(val, None, None)
            q.append(newNode)

            node = node.next

        
        for index, vertex in enumerate(olist):
            if vertex.random:
                random_index = olist.index(vertex.random)
                q[index].random = q[random_index]
    
            if index < len(q) - 1:
                q[index].next = q[index+1]

        return q[0]


        




"""
            val = node.val
            rand = node.random
            rindex = None
            if rand:
                rindex = rand.val
            hm[val, rindex] = Node(val, None, None)
            q.append([val, rindex])
            if node == head:
                newhead = hm[val, rindex]
            node = node.next

        prev = None
        for t in q:
            node = hm[t[0], t[1]]
            if prev:
                prev.next = node #establishes next ptr
            node.random = hm
 
            prev = node
"""


