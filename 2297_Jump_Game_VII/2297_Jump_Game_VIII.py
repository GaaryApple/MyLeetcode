"""
Question:
You are given a 0-indexed integer array nums of length n. You are initially standing at index 0. You can jump from index i to index j where i < j if:

nums[i] <= nums[j] and nums[k] < nums[i] for all indexes k in the range i < k < j, or
nums[i] > nums[j] and nums[k] >= nums[i] for all indexes k in the range i < k < j.
You are also given an integer array costs of length n where costs[i] denotes the cost of jumping to index i.

Return the minimum cost to jump to the index n - 1.

Soln:
dp solution
case 1: next great element 
case 2: next small element 
for each index i, two cases to jump 
"""
class Solution(object):
    def minCost(self, nums, costs):
        """
        :type nums: List[int]
        :type costs: List[int]
        :rtype: int
        """
        n = len(nums)
        ngi = [n] * n
        nsi = [n] * n
        ngs = []
        nes = []
        for i in range(n):
            while ngs and nums[ngs[-1]] <= nums[i]:
                ngi[ngs.pop()] = i
            while nes and nums[nes[-1]] > nums[i]:
                nsi[nes.pop()] = i
            ngs.append(i)
            nes.append(i)

        dp = [float("inf")] * n
        dp[0] = 0

        for i in range(n):
            for j in [ngi[i], nsi[i]]:
                if j < n:
                    dp[j] = min(dp[j], dp[i] + costs[j])
        return dp[-1]