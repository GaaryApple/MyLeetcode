"""
Question:

A k-booking happens when k events have some non-empty intersection (i.e., there is some time that is common to all k events.)

You are given some events [start, end), after each given event, return an integer k representing the maximum k-booking between all the previous events.

Implement the MyCalendarThree class:

MyCalendarThree() Initializes the object.
int book(int start, int end) Returns an integer k representing the largest integer such that there exists a k-booking in the calendar.

Idea:
Build calendar using segment tree - lazy  contructs child if necessary
tot indicate counts of overlap given period
"""

class Node():
    def __init__(self, start, end, tot = 0):
        self.start = start
        self.end = end
        self.tot = tot
        self.left = self.right = None

    def push(self):
        self.tot +=1
        if self.left:
            self.left.push()
        if self.right:
            self.right.push()

    def update(self, left, right):
        if left == self.start and right == self.end:
            self.tot +=1
            if self.left:
                self.left.push()
            if self.right:
                self.right.push()
            return self.tot
        mid = (self.start + self.end)//2
        if not self.left and not self.right:
            self.left = Node(self.start, mid, self.tot)
            self.right = Node(mid+1, self.end, self.tot)
        if right <= mid:
            self.tot =  max(self.tot, self.left.update(left, right))
        elif left > mid:
            self.tot = max(self.tot, self.right.update(left, right))
        else:
            l = self.left.update(left, mid)
            r = self.right.update(mid+1, right)
            self.tot = max(self.tot, l, r)
        return self.tot

class MyCalendarThree(object):
    def __init__(self):
        self.root = Node(0, 10**9)

    def book(self, start, end):
        return self.root.update(start, end-1)



