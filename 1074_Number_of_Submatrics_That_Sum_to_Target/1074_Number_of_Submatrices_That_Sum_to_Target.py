"""
Question:
Given a matrix and a target, return the number of non-empty submatrices that sum to target.

A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.

Soln:
presum idea
"""
class Solution(object):
    def numSubmatrixSumTarget(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        ans = 0
        for left in range(n):
            right = left
            presum = [0] * m
            while right < n:
                for i in range(m):
                    presum[i] += matrix[i][right]
                count = self.numSubArraySumTarget(presum, target)
                ans += count
                right +=1

        return ans


    def numSubArraySumTarget(self, nums, target):
        d = {0:1}
        cur = 0
        ans = 0
        for num in nums:
            cur += num
            ans += d.get(cur-target, 0)
            d[cur] = d.get(cur, 0) + 1
        
        return ans