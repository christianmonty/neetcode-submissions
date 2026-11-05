# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:

        # could repeatedly call recurse(), and once returns nothing, then we're done
        # call recurse() on root, append return values to outlist

        # I needed assistance to fix bugs and get this working

        outlist = []

        def recurse(node: Optional[TreeNode]) -> List[int]:
            if not node:
                return []
            if not node.left and not node.right:
                return [node.val]

            left_leaf = node.left and not node.left.left and not node.left.right
            right_leaf = node.right and not node.right.left and not node.right.right

            leftlist = recurse(node.left)
            rightlist = recurse(node.right)
            if left_leaf:
                node.left = None
            if right_leaf:
                node.right = None
            return leftlist + rightlist # combine the lists

            
        while True:
            if root and not root.left and not root.right:
                outlist.append([root.val])
                break
            retlist = recurse(root)
            if retlist:
                outlist.append(retlist)
            

        return outlist


        '''
        def delete(node: Optional[TreeNode], value: int):
            if not node or node.val == value:
                return
            if node.left and node.left.val == value:
                node.left = None
            else:
                delete(node.left, value)
            elif node.right and node.right.val == value:
                node.right = None
            else:
                delete(node.right, value)
    '''
        