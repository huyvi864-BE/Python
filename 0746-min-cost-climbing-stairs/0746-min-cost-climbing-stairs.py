from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        first, second = cost[0], cost[1]
        for i in range(2,len(cost)):
            first, second = second, cost[i] + min(first, second)
        return min(first, second)

        