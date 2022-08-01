"""
Question:
Given the head of a singly linked list, reverse the list, and return the reversed list.

Soln:
straigh reverse the pointer of list

"""
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        pre = None

        while cur:
            tmp = cur.next
            cur.next= pre
            pre = cur
            cur = tmp
        
        return pre
        