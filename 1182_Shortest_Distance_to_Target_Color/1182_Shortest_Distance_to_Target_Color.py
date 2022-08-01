"""
Question:
You are given an array colors, in which there are three colors: 1, 2 and 3.
You are also given some queries. Each query consists of two integers i and c, return the shortest distance between the given index i and the target color c.
If there is no solution return -1.

Soln:
Store color index using dict
binary search for each query result
"""

class Solution(object):
    def shortestDistanceColor(self, colors, queries):
        """
        :type colors: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        import bisect
        from collections import defaultdict
        d = defaultdict(list)
        res = []
        for i, color in enumerate(colors):
            d[color].append(i)
        
        for i, color in queries:
            if color not in d:
                res.append(-1)
            else:
                idx = bisect.bisect_left(d[color], i)
                if idx == len(d[color]):
                    res.append(i-d[color][-1])
                elif idx == 0:
                    res.append(d[color][0] - i)
                else:
                    res.append(min(d[color][idx]-i, i-d[color][idx-1]))

        return res 

