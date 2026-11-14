class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        min_size = len(nums)
        sum = 0
        reached = False

        for r in range(len(nums)):
            sum += nums[r]
            while sum >= target:
                reached = True
                min_size = min(min_size, r - l + 1)
                sum -= nums[l]
                l += 1
        
        if not reached:
            return 0
        else:
            return min_size
        