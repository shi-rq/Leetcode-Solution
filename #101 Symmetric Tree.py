'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3


But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3


Note:
Bonus points if you could solve it both recursively and iteratively.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 1 Iteration
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root : return True
        level1 = [root]
        level2 = []
        value = []
        empty = False
        while not empty:
            for i in level1:
                if i : level2.append(i.left)
                else : level2.append(None)
                if i : level2.append(i.right)
                else : level2.append(None)
            for i in level2:
                if i : value.append(i.val)
                else : value.append(None)
            for n in range(int(len(value) / 2)):
                if value[n] != value[-1-n] : return False
            empty = True
            for i in level2:
                if i : empty = False
            level1 = level2.copy()
            level2.clear()
            value.clear()
        return True


# 2 Recursion
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def areSymmetric(node1, node2):
            if not node1 or not node2:
                if not node1 and not node2:
                    return True
                else:
                    return False
            elif node1.val != node2.val:
                return False
            else:
                return areSymmetric(node1.left, node2.right) and areSymmetric(node1.right, node2.left)

        if not root:
            return True
        else:
            return areSymmetric(root.left, root.right)