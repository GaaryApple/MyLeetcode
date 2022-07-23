"""
Question:
You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. 
You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Return true if you can make this square and false otherwise.


Soln:
if sum of nums can't divided by 4 then False
if len of nums less than 4 then False
num sort reversely 
4 containers, try each num 
"""

class Solution(object):
    def makesquare(self, matchsticks):
        """
        :type matchsticks: List[int]
        :rtype: bool
        """
        s = sum(matchsticks)
        n = len(matchsticks)
        if s%4:
            return False
        if n < 4:
            return False
        seen = [0] * 4
        matchsticks.sort(reverse = True)
        target = s/4

        def dfs(i):
            if i == n:
                return len(set(seen)) == 1
            for j in range(4):
                seen[j] += matchsticks[i]
                if seen[j] <= target and dfs(i+1):
                    return True
                seen[j] -= matchsticks[i]
                if seen[j] == 0:
                    break
            return False            
        
        return dfs(0)
