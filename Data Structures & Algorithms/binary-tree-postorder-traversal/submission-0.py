# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        stack = []
        if root:
            stack.append(root)

        res = []
        hs = set()

        while stack:
            temp = stack.pop()
            if (not temp.right and not temp.left) or temp.val in hs:
                # OR if visited
                res.append(temp.val)
            else:
                stack.append(temp)
                hs.add(temp.val)
                if temp.right:
                    stack.append(temp.right)
                if temp.left:
                    stack.append(temp.left)
        
        return res



        