'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 1 Iteration
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root : return 0
        level = [root]
        count = 1
        while level:
            level = [i.left for i in level if i.left] + [i.right for i in level if i.right]
            count += 1
        return count-1


# 2 Recursion
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root : return 0
        else : return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1