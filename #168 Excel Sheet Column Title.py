'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"
'''


# 1 Iteration
class Solution:
    def convertToTitle(self, n: int) -> str:
        digit = "0ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        reverse = ""
        while n != 0:
            if n%26 == 0:
                reverse += 'Z'
                n -= 1
            else : reverse += digit[n%26]
            n = int(n/26)
        return reverse[::-1]


# 2 Recursion
class Solution:
    def convertToTitle(self, n: int) -> str:
        digit = "0ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if n < 27 : return digit[n]
        else:
            remain = n % 26
            if remain == 0 :
                remain = 26
                n -= 1
            n = int(n/26)
            return self.convertToTitle(n) + digit[remain]