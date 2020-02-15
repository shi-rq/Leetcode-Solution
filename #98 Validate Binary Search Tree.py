'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root : return True
        elif not root.left and not root.right : return True
        elif root.left and not root.right:
            if root.left.val < root.val : return True
            else : return False
        elif not root.left and root.right:
            if root.val < root.right.val : return True
            else : return False
        else:
            return self.isValidBST(root.left) and self.isValidBST(root.right) and root.left.val < root.val and root.val < root.right.val