# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def checkBST(root, left, right):
            if not root:
                return True
            
            if root.val <= left or root.val >= right:
                return False

            return checkBST(root.left, left, root.val) and checkBST(root.right, root.val, right)
        
        return checkBST(root, -1001, 1001)

        