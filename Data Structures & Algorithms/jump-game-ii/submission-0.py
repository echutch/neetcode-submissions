class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        start = end = 0

        while end < len(nums) - 1:
            new_end = end
            for i in range(start, end + 1):
                new_end = max(new_end, i + nums[i])
            start, end = end, new_end
            print(start, end)
            jumps += 1
        return jumps
        
            
        