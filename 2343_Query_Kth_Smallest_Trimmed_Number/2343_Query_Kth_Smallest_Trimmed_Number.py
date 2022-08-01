"""
Question:
You are given a 0-indexed array of strings nums, where each string is of equal length and consists of only digits.
You are also given a 0-indexed 2D integer array queries where queries[i] = [ki, trimi]. For each queries[i], you need to:
Trim each number in nums to its rightmost trimi digits.
Determine the index of the kith smallest trimmed number in nums. If two trimmed numbers are equal, the number with the lower index is considered to be smaller.
Reset each number in nums to its original length.
Return an array answer of the same length as queries, where answer[i] is the answer to the ith query.
Note:
To trim to the rightmost x digits means to keep removing the leftmost digit, until only x digits remain.
Strings in nums may contain leading zeros.
 
Soln:
dp approach
sort queries based on number of trims, 

"""
class Solution(object):
    def smallestTrimmedNumbers(self, nums, queries):
        """
        :type nums: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(nums)
        m = len(nums[0])
        d  = list(range(n))
        for i in range(m-1, -1, -1):
            rank = {x:j for j, x in enumerate(d[-1])}
            d.append(sorted(range(n), key = lambda x: (nums[x][i], rank[x])))
        return [d[t][k-1] for k, t in queries]