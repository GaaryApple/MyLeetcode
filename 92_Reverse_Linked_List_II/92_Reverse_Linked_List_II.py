"""
Question:
Given the head of a singly linked list and two integers left and right where left <= right, 
reverse the nodes of the list from position left to position right, and return the reversed list.

Soln:
loop until start pointer; reverse linked list and connnect to each part
"""
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        pre = dummy = ListNode(-1, next = head)
        for i in range(left-1):
            pre = pre.next
        
        cur = pre.next
        node = None
        for _ in range(right +1 -left):
            tmp = cur.next
            cur.next = node
            node = cur
            cur = tmp
        
        pre.next.next, pre.next = cur, node

        return dummy.next