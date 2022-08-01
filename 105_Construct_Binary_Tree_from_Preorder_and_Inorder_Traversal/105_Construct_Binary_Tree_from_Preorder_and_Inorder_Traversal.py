"""
Question:
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree 
and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Soln:
preorder: root, left, right
inorder: left, root, right
constrct root and find left/right based on inorder index
"""
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        d = {v:i for i, v in enumerate(inorder)}
        from collections import deque
        queue = deque(preorder)
        def helper(left, right):
            if left > right:
                return 
            node = TreeNode(queue.popleft())
            idx = d[node.val]
            node.left = helper(left, idx-1)
            node.right = helper(idx+1, right)
            return node

        return helper(0, len(inorder)-1)
