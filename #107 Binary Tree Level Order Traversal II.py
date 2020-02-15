'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right,
level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root : return []
        level1 = [root]
        level2 = []
        value = [root.val]
        traversal = []
        while level1:
            traversal.append(value)
            for i in level1:
                if i.left : level2.append(i.left)
                if i.right : level2.append(i.right)
            value = [i.val for i in level2]
            level1 = level2.copy()
            level2.clear()
        traversal.reverse()
        return traversal