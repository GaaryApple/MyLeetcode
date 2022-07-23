"""
Question:
Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.
Example 1:
Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

Soln:
check sum nums can be divided by k , if not return False
check len nums is greater than/equal to k, if not return False
sort num from largest to smallest
k container
put num in container and check for solutions
time complexity n**k
"""
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        s = sum(nums)
        n = len(nums)
        if s%k: return False
        if n < k: return False
        seen = [0] * k
        target = s/k
        nums.sort(reverse = True)
        def dfs(i):
            if i == n:
                return len(set(seen)) == 1
            for j in range(k):
                seen[j] += nums[i]
                if seen[j] <= target and dfs(i+1):
                    return True
                seen[j] -= nums[i]
                if seen[j] == 0:
                    break
            return False
        return dfs(0)
