"""
Question:
Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, 
and every node has no left child and only one right child.


Soln:
inorder retrieve node tree
iteratively build new tree
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        res = []
        self.inorder_array(root, res)

        cur = dummy = TreeNode(-1)
        for num in res:
            cur.right = TreeNode(num)
            cur = cur.right
        return dummy.right

    def inorder_array(self, root, res):
        if not root:
            return []
        self.inorder_array(root.left)
        res.append(root.val)
        self.inorder_array(root.right)