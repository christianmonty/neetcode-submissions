# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balance = True

        def recurseDepth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left = recurseDepth(node.left)
            right = recurseDepth(node.right)
            if node.left:
                left += 1
            if node.right:
                right += 1
            depth = abs(left - right)
            if depth > 1:
                nonlocal balance 
                balance = False
            return max(left, right)
        
        res = recurseDepth(root)
        return balance
        