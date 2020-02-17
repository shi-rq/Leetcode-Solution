'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.



Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 1 Height: Iteration, isBalanced: Recursion
class Solution:
    def height(self, node):
        if not node: return 0
        level = [node]
        count = 1
        while level:
            level = [i.left for i in level if i.left] + [i.right for i in level if i.right]
            count += 1
        return count - 1

    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right) and abs(
                self.height(root.left) - self.height(root.right)) <= 1


# 2 Height: Recursion, isBalanced: Iteration (Inorder)
class Solution:
    def height(self, node):
        if not node:
            return 0
        else:
            return max(self.height(node.left), self.height(node.right)) + 1

    def isBalanced(self, root: TreeNode) -> bool:
        stack = []
        p = root
        while True:
            if p:
                stack.append(p)
                p = p.left
            else:
                if not stack: return True
                p = stack.pop(-1)
                if abs(self.height(p.left) - self.height(p.right)) > 1: return False
                p = p.right