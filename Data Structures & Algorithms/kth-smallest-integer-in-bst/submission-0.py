# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodeList = []
        
        def inOrder(root: Optional[TreeNode]) -> int:
            if not root:
                return None
            left = inOrder(root.left)
            nodeList.append(root.val)
            if len(nodeList) == k:
                return nodeList[k-1]
            right = inOrder(root.right)

            return left if left else right
        
        return inOrder(root)