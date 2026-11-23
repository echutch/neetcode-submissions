# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def checkBalance(node):
            if not node:
                return True, 0

            check_left, left = checkBalance(node.left)
            check_right, right = checkBalance(node.right)

            if not check_left or not check_right or abs(left - right) > 1:
                return False, -1
            else:
                return True, 1 + max(left, right)

        check, height = checkBalance(root)
        return check
            

            
        