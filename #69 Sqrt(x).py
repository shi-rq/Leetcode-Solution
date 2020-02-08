'''
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.
'''


# 1 o(n), Basic method
class Solution:
    def mySqrt(self, x: int) -> int:
        for n in range(100000):
            if n*n <= x and (n+1)*(n+1) > x:
                return n


# 2 Search by 10^n
class Solution:
    def mySqrt(self, x: int) -> int:
        # n = 0～46340
        sign = 0
        for n in range(0, 50000, 10000):
            if x >= n*n and x < (n+10000)*(n+10000):
                sign = n
                break
        for n in range(sign, sign+10000, 1000):
            if x >= n*n and x < (n+1000)*(n+1000):
                sign = n
                break
        for n in range(sign, sign+1000, 100):
            if x >= n*n and x < (n+100)*(n+100):
                sign = n
                break
        for n in range(sign, sign+100, 10):
            if x >= n*n and x < (n+10)*(n+10):
                sign = n
                break
        for n in range(sign, sign+10):
            if x >= n*n and x < (n+1)*(n+1):
                return n


# 3 o(logn), Binary search
class Solution:
    def mySqrt(self, x: int) -> int:
        # n = 0～46340
        lh, rh = 0, 46341
        mid = int((lh+rh)/2)
        while not(x >= mid*mid and x < (mid+1)*(mid+1)):
            if x < mid*mid : rh = mid
            else : lh = mid
            mid = int((lh+rh)/2)
        return mid