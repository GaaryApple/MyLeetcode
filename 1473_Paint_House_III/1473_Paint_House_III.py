"""
Question:
There is a row of m houses in a small city, each house must be painted with one of the n colors (labeled from 1 to n), some houses that have been painted last summer 
should not be painted again.

A neighborhood is a maximal group of continuous houses that are painted with the same color.

For example: houses = [1,2,2,3,3,2,1,1] contains 5 neighborhoods [{1}, {2,2}, {3,3}, {2}, {1,1}].
Given an array houses, an m x n matrix cost and an integer target where:

houses[i]: is the color of the house i, and 0 if the house is not painted yet.
cost[i][j]: is the cost of paint the house i with the color j + 1.
Return the minimum cost of painting all the remaining houses in such a way that there are exactly target neighborhoods. If it is not possible, return -1.

Soln:
dp(i, t, p) indicate min cost of painting i-th house given t differnt colors and p is prev house color
dp(i,t,p) = min(dp(i+1, t-(p!=color), color) + cost[i][color] for color in range(1, n+1)) or dp(i+1, t-(p!=houses[i]), houses[i]) if houses[i]!=0

"""
class Solution(object):
    def minCost(self, houses, cost, m, n, target):
        """
        :type houses: List[int]
        :type cost: List[List[int]]
        :type m: int
        :type n: int
        :type target: int
        :rtype: int
        """

        def dp(i, t, p):
            key = (i, t, p)
            if key in self.memo:
                return self.memo[key]
            if m-i < t or t <0:
                return float("inf")
            if t == 0 and i == m:
                return 0
            if houses[i]:
                res = dp(i+1, t-(houses[i]!=p), houses[i])
            else:
                res = min(dp(i+1, t-(p!= color), color) + cost[i][color-1] for color in range(1, n+1))
            self.memo[key] = res
            return self.memo[key]
        
        self.memo = {}
        ans = dp(0, target, None)
        return ans if ans!= float("inf") else -1