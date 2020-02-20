'''
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''


# 1 Iteration
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0: return []
        if numRows == 1: return [[1]]
        triangle = [[1], [1,1]]
        for n in range(numRows - 2):
            level = [1]
            for m in range(len(triangle[-1]) - 1):
                level.append(triangle[-1][m] + triangle[-1][m+1])
            level += [1]
            triangle += [level]
        return triangle


# 2 Iteration (Mathematics)
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for n in range(numRows):
            level = []
            for m in range(n+1):
                num = 1
                for p in range(m):
                    num *= n-p
                    num /= p+1
                level.append(int(num))
            triangle.append(level)
        return triangle


# 3 Recursion
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0: return []
        else:
            small_triangle = self.generate(numRows - 1)
            triangle = [[1]] + self.generate(numRows - 1)
            for n in range(len(small_triangle)):
                for m in range(len(small_triangle[n]) - 1):
                    triangle[n+1][m+1] += small_triangle[n][m]
                triangle[n+1] += [1]
            return triangle
