from collections import deque
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        stack = [[0, []]]

        while stack:
            i, subset = stack.pop()

            if i == len(nums):
                res.append(subset)
                continue

            stack.append([i + 1, subset])
            stack.append([i + 1, subset + [nums[i]]])
        return res
        



            
            





        