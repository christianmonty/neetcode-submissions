# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def check(node: Optional[TreeNode]) -> Tuple[int, bool]:
            if not node:
                return 0, True

            left = check(node.left)
            right = check(node.right)

            return 1 + max(left[0], right[0]), left[1] and right[1] and abs(right[0] - left[0]) < 2
        
        res, balanced = check(root)
        return balanced
        