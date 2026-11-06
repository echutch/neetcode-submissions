class Solution:
    def climbStairs(self, n: int) -> int:
        stairs = [0] * (n+1)
        for i in range(n - 1, -1, -1):
            if i == n:
                stairs[i] = 0
            elif i == n-1:
                stairs[i] = 1
            elif i == n-2:
                stairs[i] = 2
            else:
                stairs[i] = stairs[i+1] + stairs[i+2]
        return stairs[0]
        