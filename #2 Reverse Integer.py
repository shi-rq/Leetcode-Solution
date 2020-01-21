'''Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers
within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem,
assume that your function returns 0 when the reversed integer overflows.
'''


# 1 Basic Method
class Solution:
    def reverse(self, x: int) -> int:
        digit = []
        sum = 0
        flag = (x < 0)
        x *= pow(-1, flag)
        while x != 0:
            digit.insert(0, x % 10)
            x = int (x / 10)
        for i in range(len(digit)):
            sum += digit[i] * pow(10, i)
        sum *= pow(-1, flag)
        if sum < pow(-2, 31) or sum > pow(2, 31) - 1 : return 0
        return sum


# 2 Short version. Converting the original number into string, and add from the first index
class Solution:
    def reverse(self, x: int) -> int:
        sum = 0
        flag = pow(-1, (x < 0))
        x = str(x * flag)
        for n in range(len(x)):
            sum += int(x[n]) * pow(10, n)
        if sum < pow(-2, 31) or sum > pow(2, 31) - 1 : return 0
        return flag * sum
