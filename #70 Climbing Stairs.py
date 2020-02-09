'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''


# 1 Recursion (Time limit exceeded)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 : return 1
        elif n == 2 : return 2
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)
        # Either climb 1 stair from stair n-1, or climb 2 stairs from stair n-2


# 2 Iteration
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 : return 1
        elif n == 2 : return 2
        else:
            n1 = 1
            n2 = 2
            for i in range(n-2):
                n3 = n1 + n2
                n1 = n2
                n2 = n3
            return n2
        # Either climb 1 stair from stair n-1, or climb 2 stairs from stair n-2