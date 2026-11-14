class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        def canFinish(speed):
            pile_count = 0
            for pile in piles:
                pile_count += (pile + speed - 1) // speed

                if pile_count > h:
                    return False
            return True

        while l <= r:
            mid = (l + r) // 2

            if canFinish(mid):
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        return res



        