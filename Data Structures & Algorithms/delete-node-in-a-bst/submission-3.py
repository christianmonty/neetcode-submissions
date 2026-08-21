# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        # here's very elegant solution I found conceptually and implemented in my own words. Redesign next time
        if not root:
            return None

        if root.val > key:
            root.left = self.deleteNode(root.left, key) # root.left must == new subtree
        elif root.val < key:
            root.right = self.deleteNode(root.right, key) # root.right must == new subtree
        else: # found the Node!
        
            if not root.left: # handles both no children and no left children
                return root.right

            elif not root.right:
                return root.left

            # then must have two children
            temp = root.right
            while temp.left:
                temp = temp.left # want next highest one
            root.val = temp.val
            root.right = self.deleteNode(root.right, temp.val) # now delete successor node from right subtree
        return root





'''

        # initial attempt, over convoluted it w/conditionals vs. solving recursively correclty
        # try again to implement with clean solution

        # first we want to identify the parent of the node, then we can figure out how to remove

        # if it's root, update that first and promote rightmost in left subtree to top
        
        # maybe somehow return it's parent here too to be things clear...
        def findNode(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if not node:
                return None
            if node.val == key:
                return node
            retl = findNode(node.left)
            retr = findNode(node.right)

            # wait what happens to other wing below children of what you removed...! must not forget

            if retl:
                newleft = retl.left
                newright = retl.right
                if newleft:
                    node.left = newleft
                    newleft.right = newright
                elif newright:
                    node.left = newright
                    newright.left = newleft
            elif retr:
                newleft = retr.left
                newright = retr.right
                if newleft:
                    node.left = newleft
                    newleft.right = newright
                elif newright:
                    node.left = newright
                    newright.left = newleft

            return None
            

        # Now must remove nodeFound from tree, if it exists
        
        nodeFound = findNode(root)
        if not nodeFound:
            return root
        
        if nodeFound == root:
            # must first detach root
            return root.left if root.left else root.right
        elif nodeFound.val < root.val:
            return findNode(root.left)
        else:
            return findNode(root.right)


        return root
'''
