class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i, value in enumerate(nums):
            for j in range(i + 1, len(nums)):
                if (value == nums[j]):
                    return True
        return False
                
         