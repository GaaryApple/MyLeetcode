"""
Question:
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Soln:
union find num and num+1/num-1 if found and return longest children given root

"""
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def find(x):
            pa[x] = pa.setdefault(x, x)
            if pa[x] != x:
                pa[x] = find(pa[x])
            return pa[x]

        def union(x, y):
            pax, pay = find(x), find(y)
            if pax!=pay:
                pa[pax] = pay

        from collections import defaultdict
        d = defaultdict(int)
        pa = {}
        if not nums:
            return 0
        nums = set(nums)
        for num in nums:
            if num + 1 in nums:
                union(num, num+1)
            if num - 1 in nums:
                union(num, num-1)

        for num in nums:
            d[find(num)] +=1
        
        return max(d.values())