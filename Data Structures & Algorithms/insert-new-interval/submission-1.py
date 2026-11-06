class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for start, end in intervals:
            if newInterval:
                new_start, new_end = newInterval

                if end < new_start:
                    res.append([start, end])
                elif start > new_end:
                    res.append(newInterval)
                    newInterval = None
                    res.append([start, end])
                else:
                    newInterval = [min(start, new_start), max(end, new_end)]
            else:   
                res.append([start, end])

        if newInterval:
            res.append(newInterval)
        return res
        