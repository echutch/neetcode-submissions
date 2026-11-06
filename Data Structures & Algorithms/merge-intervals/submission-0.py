class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        intervals.sort()

        for curr in intervals:
            if not merged or merged[-1][-1] < curr[0]:
                merged.append(curr)
            else:
                last = merged.pop()

                start = last[0]
                end = max(last[1], curr[1])
                merged.append([start, end])


        return merged


        