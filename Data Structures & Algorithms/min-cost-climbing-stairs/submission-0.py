class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 
        #            {  0 if i >= n
        # minCost = {   cost[i] if i == n - 1 or n - 2
        #            {  cost[i] + min(minCost(i+1), minCost(i+2)) 
        # 

        n = len(cost)
        minCost = [0] * n

        for i in range(n - 1, -1, -1):
            if i == n - 1 or i == n - 2:
                minCost[i] = cost[i]
            else:
                minCost[i] = cost[i] + min(minCost[i+1], minCost[i+2])
        return min(minCost[0], minCost[1])
        