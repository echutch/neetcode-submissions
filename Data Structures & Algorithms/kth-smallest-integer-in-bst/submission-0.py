# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.kth = 0
        self.count = 0
        
        def kthSmallestHelper(root, k):
            if not root:
                return root
            
            kthSmallestHelper(root.left, k)
            self.count += 1

            if self.count == k:
                self.kth = root.val
            kthSmallestHelper(root.right, k)

        kthSmallestHelper(root, k)
        return self.kth
        