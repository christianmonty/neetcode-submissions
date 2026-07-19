# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #check left and right recursively of root
        #if root.val == subRoot.val, start recursively checking both at same time
        #maybe start going iteratively through root first, then recursive? TBD
        if not root or not subRoot:
            return False
        res = False
        if root.val == subRoot.val:
            res = self.compare(root, subRoot)
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        return left or right or res 


    
    def compare(self, c1: Optional[TreeNode], c2: Optional[TreeNode]) -> bool:
        if not c1 and not c2:
            return True
        elif not c1 or not c2:
            return False
        left = self.compare(c1.left, c2.left)
        right = self.compare(c1.right, c2.right)
        return c1.val == c2.val and left and right