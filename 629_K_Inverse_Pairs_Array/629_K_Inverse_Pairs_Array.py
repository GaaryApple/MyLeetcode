"""
Question:
For an integer array nums, an inverse pair is a pair of integers [i, j] where 0 <= i < j < nums.length and nums[i] > nums[j].
Given two integers n and k, return the number of different arrays consist of numbers from 1 to n such that there are exactly k inverse pairs. 
Since the answer can be huge, return it modulo 109 + 7.

Soln:
dp approach
dp[i][j]: given number length i, there are j inverse pair
dp[i][j] = dp[i-1][j] + dp[i-1][j-1] + ... + dp[i-1][j-i+1] and j > i
create another cumulative sum
s[i-1][j] = dp[i-1][j] + dp[i-1][j-1] + ... + dp[i-1][0]
"""

class Solution(object):
    def kInversePairs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        dp = [[1] * (k+1) for _ in range(n+1)]
        s = [[1] * (k+1) for _ in range(n+1)]
        mod = 10**9+7

        for i in range(1, n+1):
            for j in range(1, k+1):
                dp[i][j] = s[i-1][j] if j < i else (s[i-1][j] - s[i-1][j-i] )%mod
                s[i][j] = (dp[i][j] + s[i][j-1])%mod
        
        return dp[-1][-1]