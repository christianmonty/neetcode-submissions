# class TreeNode: 
    # def __init__(self, val=0, left=None, right=None): 
        # self.val = val 
        # self.left = left 
        # self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        if not root:
            return None

        pval = p.val
        qval = q.val

        def search(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if not node:
                return None
            val = node.val
            if node.val == p.val or node.val == q.val:
                return node
            elif p.val < node.val and q.val < node.val:
                return search(node.left)
            elif p.val > node.val and q.val > node.val:
                return search(node.right)
            return node

        return search(root)
            