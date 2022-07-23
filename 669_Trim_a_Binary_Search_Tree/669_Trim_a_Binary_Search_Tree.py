"""
Question:
Given the root of a binary search tree and the lowest and highest boundaries as low and high, trim the tree so that all its elements lies in [low, high]. 
Trimming the tree should not change the relative structure of the elements that will remain in the tree (i.e., any node's descendant should remain a descendant). 
It can be proven that there is a unique answer.
Return the root of the trimmed binary search tree. Note that the root may change depending on the given bounds.

Soln:
bfs over (node, parent) and update if node val outside of range
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def trimBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: TreeNode
        """
        if not root:
            return root

        from collections import deque
        queue = deque([[root, None]])
        
        while queue:
            node, parent = queue.popleft()
            if node.val < low:
                node.left = None
                if parent:
                    parent.left = node.right
                else:
                    root = node.right
            elif node.val > high:
                node.right = None
                if parent:
                    parent.right = node.left
                else:
                    root = node.left
            else:
                parent = node
            queue.extend((child, parent) for child in [node.left, node.right] if child)
        
        return root






        