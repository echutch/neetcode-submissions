class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        key_list = self.map[key]

        l, r = 0, len(key_list) - 1
        while l <= r:
            mid = (l + r) // 2

            curr_time, val = key_list[mid]
            if curr_time <= timestamp:
                res = val
                l = mid + 1
            else:
                r = mid - 1
        return res
        
