from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque()
        q.append(root)
        
        temp = []
        outlist = []

    # this breaks q pattern commonly seen, but it works! Idea from solutions...
        while q:
            qlen = len(q)
            while qlen:
                node = q.popleft()
                temp.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                qlen -=1

            outlist.append(temp)
            temp = []

        return outlist


    

        