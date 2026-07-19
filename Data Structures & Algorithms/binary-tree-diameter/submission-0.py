# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        hm = {}

        def recurseDepth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            if not node.left and not node.right:
                hm[node.val] = [0, 0]
            

            lc = recurseDepth(node.left)
            rc = recurseDepth(node.right)
            left, right = 0, 0
            if node.left:
                left = 1 + max(hm[node.left.val][0], hm[node.left.val][1])
            if node.right:
                right = 1 + max(hm[node.right.val][0], hm[node.right.val][1])
            hm[node.val] = [left, right]

            return max(left+right, lc, rc)
        

        return recurseDepth(root)