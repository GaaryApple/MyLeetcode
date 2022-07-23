
"""
Questions:
A sequence of numbers is called arithmetic if it consists of at least two elements, and the difference between every two consecutive elements is the same. More formally, a 
sequences is arithmetic if and only if s[i+1] - s[i] == s[1] - s[0] for all valid i.

For example, these are arithmetic sequences:
1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic:

1, 1, 2, 5, 7
You are given an array of n integers, nums, and two arrays of m integers each, l and r, representing the m range queries, where the ith query is the range [l[i], r[i]]. All the 
arrays are 0-indexed.

Return a list of boolean elements answer, where answer[i] is true if the subarray nums[l[i]], nums[l[i]+1], ... , nums[r[i]] can be rearranged to form an arithmetic sequence, and 
false otherwise.

Idea:
Brute-force, for each ranges, check if nums[l:r+1] is arithmetic
if max - min /(l-1) == integer
if all arithmetic nums in nums[l:r+1]

timecomplexity o(m*n) where m is length of range and n is length of nums
"""

class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        res = []
        for i in range(len(l)):
            res.append(self.checkArithmeticNums(nums[l[i]:r[i]+1]))
        return res

    def checkArithmeticNums(self, nums):
        mx, mn = max(nums), min(nums)
        if (mx-mn)%(len(nums)-1) != 0:
            return False
        numset = set(nums)
        if len(numset) != len(nums):
            return mx == mn
        dif = (mx - mn)//(len(nums)-1)
        for num in range(mn, mx, dif):
            if num not in numset:
                return False
        return True
