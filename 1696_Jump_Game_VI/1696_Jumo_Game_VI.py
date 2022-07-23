"""
Question:
You are given a 0-indexed integer array nums and an integer k.
You are initially standing at index 0. In one move, you can jump at most k steps forward without going outside the boundaries of the array. 
That is, you can jump from index i to any index in the range [i + 1, min(n - 1, i + k)] inclusive.
You want to reach the last index of the array (index n - 1). Your score is the sum of all nums[j] for each index j you visited in the array.
Return the maximum score you can get.

Soln:
dp[i]: max score at i-th, priority queue to store values

"""
class Solution(object):
    def maxResult(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import deque
        n = len(nums)
        dp = [float("-inf")] * n
        dp[0] = nums[0]
        queue = deque([[nums[0], 0]])
        for i in range(1, n):
            dp[i] = nums[i] + queue[0][0]
            while queue and dp[i] > queue[-1][0]:
                queue.pop()
            queue.append([dp[i], i])
            if i == queue[0][1] + k:
                queue.popleft()
        return dp[-1]