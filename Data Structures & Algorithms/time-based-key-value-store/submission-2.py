class TimeMap:

    def __init__(self):
        self.hash_map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        vals = self.hash_map.get(key, [])
        vals.append([value, timestamp])
        self.hash_map[key] = vals
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hash_map:
            return ""

        res = ""
        vals = self.hash_map[key]

        l, r = 0, len(vals) - 1

        while l <= r:
            mid = (l + r) // 2
            mid_val, mid_timestamp = vals[mid]

            if timestamp == mid_timestamp:
                return mid_val
            elif mid_timestamp > timestamp:
                r = mid - 1
            else:
                res = mid_val
                l = mid + 1
        return res
        
