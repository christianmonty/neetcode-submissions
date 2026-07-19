# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        outlist = [] # of values
        q = [] # of nodes
        if not root:
            return outlist
        q.append(root)
        hm = {}
        hm[root] = 0

        while q:
            node = q.pop(0)
            if not q or hm[q[0]] > hm[node]:
                outlist.append(node.val)

            if node.left:
                q.append(node.left)
                hm[node.left] = 1 + hm[node]
            if node.right:
                q.append(node.right)
                hm[node.right] = 1 + hm[node]
        
        return outlist

        