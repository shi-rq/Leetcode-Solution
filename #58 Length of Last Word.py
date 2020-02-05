'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word
(last word means the last appearing word if we loop from left to right) in the string.

If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.

Example:

Input: "Hello World"
Output: 5
'''


# 1 Note head and tail
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = " " + s
        len0 = len(s)
        i, j = len0, len0
        for n in range(len0):
            if s[len0-1-n] != " ":
                j = n
                break
        for n in range(j+1, len0):
            if s[len0-1-n] == " ":
                i = n
                break
        return i-j


# 2 Count letters
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = " " + s
        count = 0
        len0 = len(s)
        for n in range(len0):
            if s[len0-1-n] != " " :
                count += 1
                if s[len0-2-n] == " ": break
        return count