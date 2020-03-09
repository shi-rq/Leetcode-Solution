'''

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example:

Input: 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''


class Solution:
    def isHappy(self, n: int) -> bool:
        record = []
        while not n in record:
            record.append(n)
            sum = 0
            for i in str(n):
                sum += int(i) ** 2
            n = sum
            if n == 1: return True
        return False

# Improved with hash
class Solution:
    def isHappy(self, n: int) -> bool:
        record = {}
        while not record.__contains__(n):
            record[n] = None
            sum = 0
            for i in str(n):
                sum += int(i) ** 2
            n = sum
            if n == 1: return True
        return False