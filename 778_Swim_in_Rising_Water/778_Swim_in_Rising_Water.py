"""
Question:
You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).

The rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 4-directionally adjacent square if and only 
if the elevation of both squares individually are at most t. You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid 
during your swim.

Return the least time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left square (0, 0).

Soln:
union find by starting from smallest value until find(0) == find(n*n-1)

"""
class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def find(x):
            pa[x] = pa.setdefault(x,x)
            if pa[x] !=x:
                pa[x] = find(pa[x])
            return pa[x]

        def union(x, y):
            pax, pay = find(x), find(y)
            if pax != pay:
                pa[pax] = pay
        n = len(grid)
        pa = {}
        points = [(grid[i][j], i, j) for i in range(n) for j in range(n)]
        points.sort()
        seen = [[0] * n for _ in range(n)]
        for val, i, j in points:
            seen[i][j] = 1
            for x, y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if 0<=x<n and 0<=y<n and seen[x][y] == 1:
                    union(x*n+y, i*n+j)
            if find(0) == find(n*n-1):
                return val 
