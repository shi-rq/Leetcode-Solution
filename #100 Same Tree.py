'''
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 1 Breadth First
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q : return True
        if (p and not q) or (q and not p) or (p.val != q.val) : return False
        p_tree, q_tree = [p], [q]
        empty = False
        while not empty:
            p_tree = [i.left if i and i.left else None for i in p_tree] + [i.right if i and i.right else None for i in p_tree]
            q_tree = [i.left if i and i.left else None for i in q_tree] + [i.right if i and i.right else None for i in q_tree]
            p_tree_val = [i.val if i else None for i in p_tree]
            q_tree_val = [i.val if i else None for i in q_tree]
            if p_tree_val != q_tree_val : return False
            empty = True
            for i in p_tree :
                if i : empty = False
            for i in q_tree :
                if i : empty = False
        return True


# 2 Depth First (Recursion)
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p or not q:
            if not p and not q : return True
            else : return False
        elif p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)