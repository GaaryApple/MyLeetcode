"""
Question:
Given an m x n integer matrix grid, return the maximum score of a path starting at (0, 0) and ending at (m - 1, n - 1) moving in the 4 cardinal directions.
The score of a path is the minimum value in that path.
For example, the score of the path 8 → 4 → 5 → 9 is 4.
Soln:
binary search + bfs and union find by largest to smallest value

"""
class Solution(object):
    def maximumMinimumPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def possible(d):
            from collections import deque
            queue = deque([[0,0]])
            seen = [[0] * n for _ in range(m)]
            seen[0][0] = 1
            while queue:
                x, y = queue.popleft()
                if x == m-1 and y == n-1:
                    return True
                for i, j in [(x+1, y), (x-1,y), (x, y+1), (x, y-1)]:
                    if 0<=i<m and 0<=j<n and seen[i][j] == 0 and grid[i][j] >=d:
                        queue.append((i, j))
                        seen[i][j] = 1
            return False
                
        m, n = len(grid), len(grid[0])
        lo, hi = 0, min(grid[0][0], grid[-1][-1])
        while lo < hi:
            mid = (lo + hi +1)//2
            if possible(mid):
                lo = mid
            else:
                hi = mid + 1
        return lo

class Solution(object):
    def maximumMinimumPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def find(x):
            pa[x] = pa.setdefault(x, x)
            if pa[x] !=x:
                pa[x] = find(pa[x])
            return pa[x]
        
        def union(x, y):
            pax, pay = find(x), find(y)
            if pax != pay:
                pa[pax] = pay

        pa = {}
        m, n = len(grid), len(grid[0])
        nums = list(set([(grid[x][y],x, y) for x in range(m) for y in range(n)]))
        nums.sort(reverse=  True)
        seen = [[0] * n for _ in range(m)]
        for num, i, j in nums:
            seen[i][j] = 1
            for x, y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if 0<=x<m and 0<=y<n and seen[x][y]:
                    union(x*n+y, i*n+j)
            if find(0) == find(n*m-1):
                return num
