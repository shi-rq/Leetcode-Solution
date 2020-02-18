"""
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path
from the root node down to the nearest leaf node.
Note: A leaf is a node with no children.
Example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 1 Iteration
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        level1 = [root]
        level2 = []
        count = 1
        while True:
            level2 = []
            for i in level1:
                if not i.left and not i.right: return count
                if i.left: level2.append(i.left)
                if i.right: level2.append(i.right)
            level1 = level2.copy()
            level2.clear()
            count += 1


# 2 Recursion
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        elif root.left and not root.right: return self.minDepth(root.left) + 1
        elif root.right and not root.left: return self.minDepth(root.right) + 1
        else: return min(self.minDepth(root.left), self.minDepth(root.right)) + 1