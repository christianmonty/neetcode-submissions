# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right) -> bool:
            if not node:
                return True
            if not (left < node.val < right):
                return False
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)

        return valid(root, -float('infinity'), float('infinity'))












'''
        # first we'll do in-order traversal. If fails, then not valid. Next look at chidren for each node

        inorder = []
        def inOrderTraversal(node: Optional[TreeNode]):
            if not node:
                return
            nonlocal inorder

            inOrderTraversal(node.left)
            inorder.append(node.val)
            inOrderTraversal(node.right)
            return

        inOrderTraversal(root)

        i = 0
        j = i + 1
        while j < len(inorder):
            if inorder[i] >= inorder[j]:
                return False
            i += 1
            j += 1
        
        return True
'''