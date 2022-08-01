"""
Question:
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) 
You may assume all four edges of the grid are surrounded by water.
The area of an island is the number of cells with a value 1 in the island.
Return the maximum area of an island in grid. If there is no island, return 0.

Soln:
dfs search if grid[i][j] == 1 and update/avoide repetition
"""
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans = max(ans, self.dfs(i, j, grid))
        return ans

    def dfs(self, i , j, grid):
        if not (0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j] == 1):
            return 0
        grid[i][j] = -1
        return 1 + self.dfs(i+1, j, grid) + + self.dfs(i-1, j, grid) + + self.dfs(i, j+1, grid) + + self.dfs(i, j-1, grid)