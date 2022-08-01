"""
Question:
There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. 
You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). 
You can apply at most maxMove moves to the ball.

Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. 
Since the answer can be very large, return it modulo 109 + 7.

Soln:
dp question, current state depends on previous 4 states
"""
class Solution(object):
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        """
        :type m: int
        :type n: int
        :type maxMove: int
        :type startRow: int
        :type startColumn: int
        :rtype: int
        """
        dp = [[0] * m for _ in range(n)]

        for k in range(1, maxMove+1):
            tmp = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if k == 1:
                        tmp[i][j] += 1 if i == 0 else 0
                        tmp[i][j] += 1 if i == m-1 else 0
                        tmp[i][j] += 1 if j == 0 else 0
                        tmp[i][j] += 1 if j == n-1 else 0
                    else:
                        tmp[i][j] += dp[i-1][j] if i-1 >=0 else 1
                        tmp[i][j] += dp[i+1][j] if i+1 < m else 1
                        tmp[i][j] += dp[i][j-1] if j-1 >=0 else 1
                        tmp[i][j] += dp[i][j+1] if j+1 < n else 1
            dp = tmp[:]
        mod = 10**9+7
        return dp[startRow][startColumn]%mod