# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        outlist = []

        def dfs(node: Optional[TreeNode]): # return nothing since populate shared list
            if not node:
                return None
            nonlocal outlist
            dfs(node.left)
            outlist.append(node.val)
            dfs(node.right)
        
        dfs(root)
        return outlist

        