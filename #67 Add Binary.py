'''
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
'''


# 1 decimal-binary transformation
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]


# 2 Add according to binary rules
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        bit = {'1': 1, '0': 0}
        dec_reverse = [0 for n in range(max(len(a), len(b)) + 1)]
        for n in range(len(a)):
            dec_reverse[n] += bit[a[len(a)-1-n]]
        for m in range(len(b)):
            dec_reverse[m] += bit[b[len(b)-1-m]]
        for p in range(len(dec_reverse) - 1):
            if dec_reverse[p] >= 2:
                dec_reverse[p] -= 2
                dec_reverse[p+1] += 1
        if dec_reverse[-1] == 0 : dec_reverse.pop(-1)
        for i in dec_reverse[::-1]:
            result += str(i)
        return result