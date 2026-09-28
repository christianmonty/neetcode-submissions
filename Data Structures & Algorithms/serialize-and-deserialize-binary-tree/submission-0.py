# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        if not root:
            return ""
        
        q = deque()
        q.append(root)
        outstring = ""
        outstring += str(root.val) + " "

        while q:
            temp = q.popleft() # must for a queue
            if temp.left:
                q.append(temp.left)
                outstring += str(temp.left.val) + " "
            else:
                outstring += "N" + " "
            if temp.right:
                q.append(temp.right)
                outstring += str(temp.right.val) + " "
            else:
                outstring += "N" + " "
        return outstring
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        if data == "":
            return None

        nodes = data.split()

        # I think the move is doing the trick about if even or odd which child it is, odd left child, even right
        q = deque()

        firstnode = TreeNode(int(nodes[0]))

        q.append(firstnode)
        i = 1

        while q:
            temp = q.popleft()

            if i < len(nodes) and nodes[i] != "N":
                leftNode = TreeNode(int(nodes[i]))
                temp.left = leftNode
                q.append(leftNode)
            i += 1
            if i < len(nodes) and nodes[i] != "N":
                rightNode = TreeNode(int(nodes[i]))
                temp.right = rightNode
                q.append(rightNode)
            i += 1

        return firstnode









