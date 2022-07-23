""""
Question:
Given two sparse matrices mat1 of size m x k and mat2 of size k x n, return the result of mat1 x mat2. You may assume that multiplication is always possible.

Soln:
only record non-zero cell for multiplication purpose
mat_stack1 and mat_stack2: [i][j] * [x][y] iff j==x and return [i][y]
"""
class Solution(object):
    def multiply(self, mat1, mat2):
        """
        :type mat1: List[List[int]]
        :type mat2: List[List[int]]
        :rtype: List[List[int]]
        """
        m, k, n = len(mat1), len(mat1[0]), len(mat2[0])
        ans = [[0] * n for _ in range(m)]
        stack1 = [(mat1[i][j], i, j) for i in range(m) for j in range(k) if mat1[i][j]]
        stack2 = [(mat2[i][j], i, j) for i in range(k) for j in range(n) if mat2[i][j]]

        for num1, i, x, in stack1:
            for num2, y, j in stack2:
                ans[i][j] += num1*num2 if x == y else 0
        return ans
