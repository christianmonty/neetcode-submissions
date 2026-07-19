# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        if not root:
            return output
        myq = []
        cur = 0
        myq.append((root, cur))
        output.append([])
        output[cur].append(root.val)
        while myq:
            (tempNode, depth) = myq.pop(0)
            if not tempNode.left and not tempNode.right:
                continue;
            #what to do about creating new append
            if depth + 1 > len(output) - 1:
                output.append([])
            if tempNode.left:
                myq.append((tempNode.left, depth + 1))
                output[depth + 1].append(tempNode.left.val)
            if tempNode.right:
                myq.append((tempNode.right, depth + 1))
                output[depth + 1].append(tempNode.right.val)
        return output

        