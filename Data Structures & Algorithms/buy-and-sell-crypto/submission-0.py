class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = prices[0]
        profit = 0

        for p in prices:
            profit = max(profit, p - min_buy)
            min_buy = min(min_buy, p)
        return profit
            





        