# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        maxSum = float('-inf')
        def recurseSum(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            nonlocal maxSum
            lsum = recurseSum(root.left)
            rsum = recurseSum(root.right)
            maxSum = max(maxSum, root.val, root.val + lsum, root.val + rsum, root.val + lsum + rsum)
            return(root.val + max(lsum, rsum, 0))
        
        recurseSum(root)
        return maxSum









        """
        Overengineered approach
        
        def calculate(temp: Optional[TreeNode], passval: int) -> (int, bool):
            flag = False
            if not temp:
                return (float('-inf'), False)
            (left, lv) = calculate(temp.left, temp.val)
            (right, rv) = calculate(temp.right, temp.val)
            res = 0
            if lv and rv: #try all path combos
                res = max(temp.val + left, temp.val + right, temp.val)
                touchtips = temp.val + temp.left.val + temp.right.val
                if touchtips > res:
                    leftcheck = passval + temp.val + left
                    rightcheck = passval + temp.val + right
                    if touchtips > leftcheck and touchtips > rightcheck:
                        res = touchtips
                        return(max(res, left, right), False)
            elif lv: #try paths with both left or just temp
                res = max(left + temp.val, temp.val, temp.val + (temp.right.val if temp.right else 0))
            elif rv: #try paths with both right or just temp
                res = max(right + temp.val, temp.val, temp.val + (temp.left.val if temp.left else 0))
            else: # try just temp.val
                res = temp.val
            
            if res >= left and res >= right:
                return (res, True)
            elif res >= left:
                return (right, False)
            else:
                return (left, False)
        
        (finalres, finalv) = calculate(root, float('-inf'))
        return finalres
        """