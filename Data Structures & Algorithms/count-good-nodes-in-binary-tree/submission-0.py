# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        num = 0

        def checkNode(vl: int, node: TreeNode):
            if not node:
                return
            nonlocal num
            if vl <= node.val:
                num += 1
                checkNode(node.val, node.left)
                checkNode(node.val, node.right)
            else:
                checkNode(vl, node.left)
                checkNode(vl, node.right)

        checkNode(root.val, root)
        return num
        