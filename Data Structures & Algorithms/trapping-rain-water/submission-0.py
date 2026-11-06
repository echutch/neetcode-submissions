class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        pre = [0] * n
        post = [0] * n

        pre[0] = height[0]
        for i in range(1, n):
            pre[i] = max(pre[i-1], height[i])

        post[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            post[i] = max(post[i+1], height[i])

        res = 0
        for i in range(n):
            res += min(pre[i], post[i]) - height[i]
        return res
        