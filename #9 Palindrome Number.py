'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?
'''


# 1 Basic Method
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 : return False
        x = str(x)
        for n in range(int(len(x) / 2)):
            if x[n] != x[len(x) - 1 - n] : return False
        return True


# 2 Recursion Method
class Solution:
    def str_isPalindrome(self, x: str):
        length = len(x)
        if length == 0:
            return True
        elif length == 1:
            return True
        else:
            judge = (x[0] == x[length - 1])
            return judge and self.str_isPalindrome(x[1: length - 1])

    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        x = str(x)
        return self.str_isPalindrome(x)


# 3 Using reverse() function
# Note: So-called 'variables' in python are just 'references'. If y=x, x.reverse(), then y is also reversed.
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = list(str(x))
        y1 = x.copy()   # use copy() instead of mere assignment
        y2 = x.copy()
        y1.reverse()
        if y1 == y2 : return True
        return False