"""
Question:
Given an integer n, return all the strobogrammatic numbers that are of length n. You may return the answer in any order.
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
Example 1:
Input: n = 2
Output: ["11","69","88","96"]

Soln:
when n = 1: [0, 1, 8]
when n = 2: [00, 11, 69, 88, 96]
when n = 3: [101, 609,, 808, 906, 111, 619, 818, 916, 181, 689, 888, 986]
when n = 4: [1001, 6009, 8008, ... ]
"""
class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        odd = ['0', '1', '8']
        even = ['11', '69', '88', '96', '00']

        if n == 1:
            return odd
        elif n == 2:
            return even[:-1]
        else:
            if n%2 == 1:
                pre, cand = self.findStrobogrammatic(n-1), odd
            else:
                pre, cand = self.findStrobogrammatic(n-2), even
        
        mid = (n-1)//2
        return [p[:mid] + ch + p[mid:] for ch in cand for p in pre]
        