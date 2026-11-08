class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        merged = []
        merged.append(intervals[0])

        for start, end in intervals:
            last_end = merged[-1][1]
            if last_end >= start:
                merged[-1][1] = max(last_end, end)
            else:
                merged.append([start, end])

        return merged
        