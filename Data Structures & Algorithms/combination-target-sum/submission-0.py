class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        stack = [[0, []]]

        while stack:
            i, combo = stack.pop()
            val = sum(combo)

            if i >= len(nums) or val > target:
                continue
            
            if val == target and combo not in res:
                res.append(combo) 
                continue

            stack.append([i, combo + [nums[i]]])
            stack.append([i + 1, combo + [nums[i]]])
            stack.append([i + 1, combo])
        return res
        