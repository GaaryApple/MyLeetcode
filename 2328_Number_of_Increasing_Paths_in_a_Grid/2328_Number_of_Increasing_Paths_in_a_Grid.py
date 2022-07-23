"""
Question:
You are given an m x n integer matrix grid, where you can move from a cell to any adjacent cell in all 4 directions.
Return the number of strictly increasing paths in the grid such that you can start from any cell and end at any cell. Since the answer may be very large, return it modulo 109 + 7.
Two paths are considered different if they do not have exactly the same sequence of visited cells.

Example 1:
Input: grid = [[1,1],[3,4]]
Output: 8
Explanation: The strictly increasing paths are:
- Paths with length 1: [1], [1], [3], [4].
- Paths with length 2: [1 -> 3], [1 -> 4], [3 -> 4].
- Paths with length 3: [1 -> 3 -> 4].
The total number of paths is 4 + 3 + 1 = 8.

Idea:
    dfs search each cell and include self.memo to avoid recomputing
"""
class Solution(object):
    def countPaths(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(i, j):
            key = (i,j)
            if key in self.memo:
                return self.memo[key]
            res = 1
            for x, y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if 0<=x<m and 0<=y<n and grid[x][y] < grid[i][j]:
                    res += dfs(x, y)
            self.memo[key] = res
            return self.memo[key]
        mod = 10**9+7
        self.memo = {}
        res = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                res += dfs(i, j)
        return res%mod

