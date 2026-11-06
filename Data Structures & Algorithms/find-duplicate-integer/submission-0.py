class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        saved = {}

        for n in nums:
            if n in saved:
                return n
            else:
                saved[n] = 1
        return -1
        