"""
Question:
Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.
Implement the FreqStack class:
FreqStack() constructs an empty frequency stack.
void push(int val) pushes an integer val onto the top of the stack.
int pop() removes and returns the most frequent element in the stack.
If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.

Soln:
two dict, one for freq of each val, another is vals per freq
"""

class FreqStack(object):

    def __init__(self):
        from collections import defaultdict
        self.stack = defaultdict(list)
        self.freq = defaultdict(int)
        self.maxf = 0

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.freq[val] +=1
        self.stack[self.freq[val]].append(val)
        self.maxf = max(self.maxf, self.freq[val])

    def pop(self):
        """
        :rtype: int
        """
        x = self.stack[self.maxf].pop()
        if not self.stack[self.maxf]:
            self.maxf -=1
        self.freq[x] -=1
        return x