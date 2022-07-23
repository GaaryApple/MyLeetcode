
"""
Question:
Given n orders, each order consist in pickup and delivery services. 
Count all valid pickup/delivery possible sequences such that delivery(i) is always after of pickup(i). 
Since the answer may be too large, return it modulo 10^9 + 7.


Soln:
for each n, 2*n spots and 2n! 
to ensure pick up go before delievry for each pair /2**n
"""
class Solution(object):
    def countOrders(self, n):
        """
        :type n: int
        :rtype: int
        """
        mod = 10**9+7
        res = 1
        for i in range(1, 2*n+1):
            res *= i
        res = res/(2**n)
        return res%mod
        