class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        pre = 1
        for i in range(1, n):
            pre = pre * nums[i - 1]
            res[i] = pre

        post = 1
        for i in range(n - 2, -1, -1):
            post = post * nums[i + 1]
            res[i] *= post
        
        return res

        