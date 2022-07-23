"""
Question:
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order 
among all possible results.

Example 1:
Input: s = "bcabc"
Output: "abc"

Soln:
if stack[-1] > ch and d[stack[-1]] > i, then pop else keep
"""


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import defaultdict
        d = defaultdict(int)
        stack = []
        seen = set()
        for idx, ch in enumerate(s):
            d[ch] = idx

        for i, x in enumerate(s):
            if x not in seen:
                while stack and stack[-1] > x and d[stack[-1]] > i:
                    seen.remove(stack.pop())
                stack.append(x)
                seen.add(x)
        return "".join(stack)
