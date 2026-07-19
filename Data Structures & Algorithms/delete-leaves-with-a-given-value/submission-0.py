# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        # one idea is you have helper function amLeaf(node) where returns true if have no children and == target
        # then caller deletes that leaf, checks other side and if suddenly a leaf and == target, returns True
        # returning true means "delete me" else returning False means do not delete me

        def isLeaf(node: Optional[TreeNode]) -> bool:
            if not node:
                return False
            if node.left:
                retl = isLeaf(node.left)
                if retl:
                    node.left = None
            if node.right:
                retr = isLeaf(node.right)
                if retr:
                    node.right = None
            if not node.left and not node.right and node.val == target:
                return True
            return False

        val = isLeaf(root)
        if val:
            return None
        return root
        