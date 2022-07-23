"""
Given two integer arrays pushed and popped each with distinct values, return true if this could have been the result of a sequence
of push and pop operations on an initially empty stack, or false otherwise.
Example 1:
Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true

Soln:
for each num in pushed, append to stack
if stack[-1] == popped[0], j+=1 and pop stack
check stack is empty as final step

"""
class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        j = 0
        n = len(popped)
        for num in pushed:
            stack.append(num)
            while stack[-1] == popped[j]:
                j+=1
                stack.pop()
        return len(stack) == 0