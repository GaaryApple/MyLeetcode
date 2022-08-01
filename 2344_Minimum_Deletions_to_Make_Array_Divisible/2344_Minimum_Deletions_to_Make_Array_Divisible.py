"""
Question:
You are given two positive integer arrays nums and numsDivide. You can delete any number of elements from nums.

Return the minimum number of deletions such that the smallest element in nums divides all the elements of numsDivide. If this is not possible, return -1.

Note that an integer x divides y if y % x == 0.

Soln:
calculate gcd of numaDivide
sort nums and find first num matching gcd%num == 0 else -1
"""

class Solution(object):
    def minOperations(self, nums, numsDivide):
        """
        :type nums: List[int]
        :type numsDivide: List[int]
        :rtype: int
        """
        ans = 0
        nums.sort()
        gcd_cand = numsDivide[0]
        for cand in numsDivide[1:]:
            gcd_cand = self.gcd(gcd_cand, cand)
        for num in nums:
            if num > gcd_cand:
                return -1
            if gcd_cand % num == 0:
                return ans
            ans +=1
        return -1
    
    def gcd(self, a, b):
        if b == 0:
            return abs(a)
        else:
            return self.gcd(b, a%b)