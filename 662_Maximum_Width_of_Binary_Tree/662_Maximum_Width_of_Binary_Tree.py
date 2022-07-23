"""
Question:
Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

It is guaranteed that the answer will in the range of a 32-bit signed integer.

Soln:
bfs search adn get max width for each layer
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        from collections import deque
        queue = deque([[root, 1]])
        ans = 0
        while queue:
            left = right = None
            for _ in range(len(queue)):
                node, idx = queue.popleft()
                if not left:
                    left = idx
                if left:
                    right = idx
                if node.left:
                    queue.append((node.left, idx*2-1))
                if node.right:
                    queue.append((node.right, idx*2))
            ans = max(ans, right - left+1)
        return ans
