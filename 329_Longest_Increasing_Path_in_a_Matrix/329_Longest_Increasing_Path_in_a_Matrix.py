"""
Question:
Given an m x n integers matrix, return the length of the longest increasing path in matrix.
From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).


Idea: count of neighbors less than cell, bfs from smallest number and check each nei if possible until the end

"""

class LPM(object):
    def longestIncreasingPath(self, matrix):
        from collections import defaultdict
        from collections import deque
        queue = deque([])
        d = defaultdict(int)
        m ,n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                count = 0
                for x, y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                    if 0<=x<m and 0<=y<n and matrix[x][y] < matrix[i][j]:
                        count+=1
                d[(i,j)] = count
                if count == 0:
                    queue.append((i,j))
        step = 0
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for x, y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                    if 0<=x<m and 0<=y<n and matrix[x][y] > matrix[i][j]:
                        d[(x,y)] -=1
                        if d[(x,y)] == 0:
                            queue.append((x,y))
            step +=1

        return step
