class Solution:
    def rob(self, nums: List[int]) -> int:
        """      {nums[i] if i == n - 1 or i == n - 2
        rob(i) = {max(rob[i+1], nums[i] + rob[i+2]) else
        """         
        n = len(nums)
        rob = [0] * n
        
        for i in range(n -1, -1, -1):
            if i == n - 1 or i == n - 2:
                rob[i] = nums[i]
            else:
                rob[i] = max(rob[i+1], nums[i] + rob[i+2])
        print(rob)
        return max(rob[0], rob[1]) if n > 1 else rob[0]
        