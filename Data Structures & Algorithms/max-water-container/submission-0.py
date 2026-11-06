class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1

        max_ = 0
        while j > i:
            area = (j - i) * min(heights[i], heights[j])
            max_ = max(max_, area)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return max_
        