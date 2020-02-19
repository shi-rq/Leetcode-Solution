"""
For a non-negative integer X, the array-form of X is an array of its digits in left to right
order.  For example, if X = 1231, then the array form is [1,2,3,1].
Given the array-form A of a non-negative integer X, return the array-form of the integer X+K.

Example 1:
Input: A = [1,2,0,0], K = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234

Example 2:
Input: A = [2,7,4], K = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455

Example 3:
Input: A = [2,1,5], K = 806
Output: [1,0,2,1]
Explanation: 215 + 806 = 1021

Example 4:
Input: A = [9,9,9,9,9,9,9,9,9,9], K = 1
Output: [1,0,0,0,0,0,0,0,0,0,0]
Explanation: 9999999999 + 1 = 10000000000

"""


# 1 list -> str -> int
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        a_str = ""
        for i in A: a_str += str(i)
        a_int = int(a_str) + K
        return [int(i) for i in str(a_int)]


# 2 Basic method
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        index = -1
        while K != 0 :
            if len(A) + index == 0: A = [0] + A
            A[index] += K%10
            if A[index] >= 10:
                A[index] -= 10
                A[index-1] += 1
            K = int(K / 10)
            index -= 1
        while A[index] >= 10:
            if len(A) + index == 0: A = [0] + A
            A[index] -= 10
            A[index-1] += 1
            index -= 1
        if A[0] == 0 and len(A) > 1: A.pop(0)
        return A