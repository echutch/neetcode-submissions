class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        stack = [[0, [], 0]]

        while stack:
            i, combo, val = stack.pop()
            
            if i >= len(nums) or val > target:
                continue
            
            if val == target:
                res.append(combo) 
                continue

            stack.append([i, combo + [nums[i]], val + nums[i]])
            stack.append([i + 1, combo, val])
        return res
        