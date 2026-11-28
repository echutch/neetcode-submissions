class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        rob_vals = [0] * len(nums)
        

        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                rob_vals[i] = nums[i]
            elif i == len(nums) - 2:
                rob_vals[i] = max(rob_vals[i+1], nums[i])
            else:
                rob_vals[i] = max(rob_vals[i + 1], nums[i] + rob_vals[i + 2])

        return max(rob_vals[0], rob_vals[1])
        