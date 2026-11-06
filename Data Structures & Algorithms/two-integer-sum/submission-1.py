class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        saved_nums = {}

        for i, num in enumerate(nums):
            if target - num in saved_nums:
                return [saved_nums[target - num], i]
            else:
                saved_nums[num] = i
        