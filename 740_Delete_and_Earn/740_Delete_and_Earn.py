"""
Question:
You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:
Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
Return the maximum number of points you can earn by applying the above operation some number of times.

Idea:
backward starting from max number, number[-1]
dp[i] = max(dp[i+1], dp[i+2] + number[i])

"""
class Solution(object):
    def deleteAndEarn(self, nums):
        mx = max(nums)
        number = [0] * (mx+1)
        for num in nums:
            number[num] += num
        n = len(number)
        #dp[n] = 0 for pseudo, avoide out of bondary
        dp = [0] * (n+1)
        dp[n-1] = number[n-1]
        for i in range(n-2, -1, -1):
            dp[i] = max(dp[i+1], dp[i+2] + number[i])
        return dp[0]