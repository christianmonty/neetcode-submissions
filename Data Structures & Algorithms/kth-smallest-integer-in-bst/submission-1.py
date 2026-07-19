# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0

        def inOrder(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            nonlocal count
            ret = inOrder(node.left)
            if ret:
                return ret
            count += 1
            if count == k:
                return node.val
            ret = inOrder(node.right)
            return ret

        return inOrder(root)