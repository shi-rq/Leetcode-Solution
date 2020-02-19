"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding
up all the values along the path equals the given sum.

Note: A leaf is a node with no children.
Example:
Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1

return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 1 Recursion
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root: return False
        elif not root.left and not root.right:
            if root.val == sum: return True
            else: return False
        else: return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)


# 2 Iteration (BFS)
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root: return False
        queue = [[root, sum]]
        while queue:
            node = queue.pop(0)
            if not node[0].left and not node[0].right and node[1] == node[0].val: return True
            if node[0].left: queue.append([node[0].left, node[1]-node[0].val])
            if node[0].right: queue.append([node[0].right, node[1]-node[0].val])
        return False


# Failed Iteration (Inorder)
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        stack = []
        p = root
        while True:
            if p:
                stack.append(p)
                p = p.left
            else:
                if not stack: return False
                p = stack.pop()
                if not p.left and not p.right:
                    sum0 = 0
                    for i in stack:
                        sum0 += i.val
                    if sum0 + p.val == sum: return True
                p = p.right