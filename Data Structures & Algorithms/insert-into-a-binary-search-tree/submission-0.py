# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val, None, None)
        if val > root.val:
            # recurse right
            if root.right:
                self.insertIntoBST(root.right, val)
            else:
                root.right = TreeNode(val, None, None)
        else:
            # recurse left
            if root.left:
                self.insertIntoBST(root.left, val)
            else:
                root.left = TreeNode(val, None, None)
        return root
            