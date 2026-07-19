# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root == None or p == None or q == None:
            return None
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and not right and root.val != p.val and root.val != q.val: #first compare to root?
            return left
        if right and not left and root.val != p.val and root.val != q.val: 
            return right
        if root.val == p.val or root.val == q.val or left and right:
            return root
        return None
        
'''
        if (left.val == p.val or right.val == p.val) and root.val == q.val:
            return q
        elif (left.val == q.val or right.val == q.val) and root.val == p.val:
            return p
        elif (left.val == p.val and right.val == q.val) or (left.val == q.val and right.val == p.val) or root.val == p.val or root.val == q.val:
            return root
        return left if left else right
'''