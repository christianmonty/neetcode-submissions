# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        minm = {}
        maxm = {}

        q = []
        q.append(root)
        while q:
            temp = q.pop(0)
            if temp.val in minm and temp.val <= minm[temp.val] or temp.val in maxm and temp.val >= maxm[temp.val]:
                return False
            if temp.left:
                if temp.val in minm:
                    minm[temp.left.val] = minm[temp.val]
                maxm[temp.left.val] = temp.val
                q.append(temp.left)
            if temp.right:
                if temp.val in maxm:
                    maxm[temp.right.val] = maxm[temp.val]
                minm[temp.right.val] = temp.val
                q.append(temp.right)
        return True