'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
'''


# 1 Confirm bit by bit
class Solution:
    def isPalindrome(self, s: str) -> bool:
        lh ,rh = 0, len(s)-1
        while lh < rh:
            while not ((s[lh]>='a' and s[lh]<='z') or (s[lh]>='A' and s[lh]<='Z') or (s[lh]>='0' and s[lh]<='9')):
                lh += 1
                if lh == rh: return True
            while not ((s[rh]>='a' and s[rh]<='z') or (s[rh]>='A' and s[rh]<='Z') or (s[rh]>='0' and s[rh]<='9')) :
                rh -= 1
                if rh == lh: return True
            if s[lh].lower() != s[rh].lower() :
                return False
            lh += 1
            rh -= 1
        return True


# 2 Expire invalid characters
class Solution:
    def isPalindrome(self, s: str) -> bool:
        pickup = [i.upper() for i in s if (i>='a' and i<='z') or (i>='A' and i<='Z') or (i>='0' and i<='9')]
        if pickup == pickup[::-1] : return True
        else : return False