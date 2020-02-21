'''
Given a non-negative index k where k <= 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?
'''


# 1 Mathematics
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = []
        for n in range(rowIndex + 1):
            num = 1
            for m in range(n):
                num *= rowIndex-m
                num /= m+1
            row.append(int(num))
        return row


# 2 Iteration
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: return [1]
        row = [1, 1]
        while len(row) <= rowIndex:
            for n in range(len(row) - 1):
                row[n] = row[n] + row[n+1]
            row = [1] + row
        return row