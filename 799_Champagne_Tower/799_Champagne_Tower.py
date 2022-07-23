"""
Question:
We stack glasses in a pyramid, where the first row has 1 glass, the second row has 2 glasses, and so on until the 100th row.  Each glass holds one cup of champagne.
Then, some champagne is poured into the first glass at the top.  When the topmost glass is full, any excess liquid poured will fall equally to the glass immediately to 
the left and right of it.  When those glasses become full, any excess champagne will fall equally to the left and right of those glasses, and so on.  
(A glass at the bottom row has its excess champagne fall on the floor.)

For example, after one cup of champagne is poured, the top most glass is full.  After two cups of champagne are poured, the two glasses on the second row are half full.  
After three cups of champagne are poured, those two cups become full - there are 3 full glasses total now.  After four cups of champagne are poured, the third row has the 
middle glass half full, and the two outside glasses are a quarter full, as pictured below.

Now after pouring some non-negative integer cups of champagne, return how full the jth glass in the ith row is (both i and j are 0-indexed.)

Soln:
dp = [poured] + [0] * query_row

cur_dp[i]: 0.5*(pre_dp[i]-1) + 0.5*(pre_dp[i-1]-1)
for each row,  starting from i and i-1, ..., 0 update
"""
class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        dp = [poured] + [0] * query_row

        for row in range(1, query_row+1):
            for j in range(row, -1, -1):
                dp[j] = max(dp[j] - 1, 0)/2.0 + max(dp[j-1] - 1, 0)/2.0

        return min(dp[query_glass], 1)