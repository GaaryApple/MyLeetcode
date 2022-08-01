"""
Question:
Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree of distinct values and postorder 
is the postorder traversal of the same tree, reconstruct and return the binary tree.

If there exist multiple answers, you can return any of them.

Soln:
preorder: root, left, right
postorder: left, right, root
first build leftmost tree and move on to next
leftmost node can be checked using postorder
"""
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def constructFromPrePost(self, preorder, postorder):
        """
        :type preorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        stack = []
        j = 0
        n = len(preorder)
        for i in range(n):
            node = TreeNode(preorder[i])
            while stack and stack[-1].val == postorder[j]:
                stack.pop()
                j+=1
            if stack and not stack[-1].left:
                stack[-1].left = node
            elif stack and not stack[-1].right:
                stack[-1].right = node
            stack.append(node)

        return stack[0]