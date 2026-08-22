# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # root must be first in preorder
        # noticing: in-order shows what is on left or right of each parent node. Left of parent is left, right is right
        # pre-order is top down, but knowing what children is from in order
        # [ 1 2 3 4] pre-order
        # [ 2 1 3 4] in-order # well here we know that left subtree must be indices [0:1] and right subtree must be [2::]
        # so maybe what you should recurse is left half as left child, right half as right child

        # part I missed in this solution is recursively having left bounds to left of root, right bounds to right of root
        # it's almost like 2 pointers thinking within a Tree problem, which makes is tricky but good problem

        hm = {}
        for index, val in enumerate(inorder):
            hm[val] = index # works since consists of unique values
            # given a value in the tree, result index order from in-order

        index = 0

        def recurse(left: int, right: int) -> Optional[TreeNode]: # to return to root directly, or None
            # with left and right the bounds of subtree
            if left > right: # done with subtree, return
                return None

            nonlocal index
            nextval = preorder[index]
            curind = hm[nextval] # index of current value within in-order
            node = TreeNode(nextval)


            index += 1 # do we need a nonlocal?
            node.left = recurse(left, curind - 1)
            node.right = recurse(curind + 1, right)
            return node
        

        return recurse(0, len(preorder) - 1)
            
