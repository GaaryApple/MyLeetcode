"""
Question:
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and 
postorder is the postorder traversal of the same tree, construct and return the binary tree.

Soln:
inorder: left, root, right
postorder: left, right, root
"""
#Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        d = {ch:idx for idx, ch in enumerate(inorder)}
        stack = postorder

        def helper(left, right):
            if left > right:
                return 
            node = TreeNode(stack.pop())
            idx = d[node.val]
            node.right = helper(idx+1, right)
            node.left = helper(left, idx-1)
            return node

        return helper(0, len(inorder)-1)
         