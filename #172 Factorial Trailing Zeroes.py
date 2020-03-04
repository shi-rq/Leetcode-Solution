'''
Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Note: Your solution should be in logarithmic time complexity.
'''


# 1 Basic method
class Solution:
    def trailingZeroes(self, n: int) -> int:
        num = 1
        for m in range(n):
            num *= m+1
        count = 0
        for i in str(num)[::-1]:
            if i == '0' : count += 1
            else : return count


# 2 Count 5
class Solution:
    def trailingZeroes(self, n: int) -> int:
        powered = 5
        count = 0
        while powered <= n:
            count += int(n / powered)
            powered *= 5
        return count