# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def checkBalance(root):
            if not root:
                return 0

            check_left = checkBalance(root.left)
            check_right = checkBalance(root.right)

            if check_left < 0 or check_right < 0 or abs(check_left - check_right) > 1:
                return -1
            
            return 1 + max(check_left, check_right)
        return True if checkBalance(root) >= 0 else False
            

            
            
        
        