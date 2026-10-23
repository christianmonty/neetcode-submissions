# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def equalToDescendants(self, root: TreeNode) -> int:

        def recurse(node: TreeNode) -> (int, int):
            if not node:
                return 0, 0
            if not node.left and not node.right:
                if node.val == 0:
                    return 0, 1
                return node.val, 0

            leftval, leftnum = recurse(node.left)
            rightval, rightnum = recurse(node.right)

            if node.val == leftval + rightval:
                return node.val * 2, 1 + leftnum + rightnum
            return node.val + leftval + rightval, leftnum + rightnum
        
        _, totalnum = recurse(root)
        return totalnum
