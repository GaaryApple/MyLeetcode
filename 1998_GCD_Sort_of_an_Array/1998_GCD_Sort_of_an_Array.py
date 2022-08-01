"""
Question:
You are given an integer array nums, and you can perform the following operation any number of times on nums:
Swap the positions of two elements nums[i] and nums[j] if gcd(nums[i], nums[j]) > 1 where gcd(nums[i], nums[j]) is 
the greatest common divisor of nums[i] and nums[j].
Return true if it is possible to sort nums in non-decreasing order using the above swap method, or false otherwise.

Soln:
graph + unionfind
for num in nums, find all divisible prime numbers and union num and prime factor
for i, j in zip(nums, sorted(nums)), check if they are connected 
"""
class Solution(object):
    def gcdSort(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def find(x):
            pa[x] = pa.setdefault(x, x)
            if pa[x] != x:
                pa[x] = find(pa[x])
            return pa[x]
        
        def union(x, y):
            pax, pay = find(x), find(y)
            if pax != pay:
                pa[pax] = pay
        pa = {}
        for num in nums:
            p = 2
            y = num
            while y not in pa and p**2 <=y:
                if y%p == 0:
                    union(num, p)
                    while y%p ==0:
                        y = y//p
                p+=1
            if y!=1:
                union(num, y)

        for i, j in zip(nums, sorted(nums)):
            if find(i)!= find(j):
                return False
        return True