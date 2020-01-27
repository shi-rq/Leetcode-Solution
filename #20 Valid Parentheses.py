'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
'''


# 1 Stack
class Solution:
    def isValid(self, s: str) -> bool:
        pair = {"(": 0, "[": 0, "{": 0, ")": "(", "]": "[", "}": "{"}
        # ([{ -> False;   )]} -> True
        stack = []
        for i in s:
            if not pair[i] : stack.append(i)
            else:
                if not stack or pair[i] != stack[-1] : return False
                else : stack.pop(-1)
        if stack : return False
        else: return True


# 2 Replace, simple but slow
class Solution:
    def isValid(self, s: str) -> bool:
        while("()" in s or "[]" in s or "{}" in s):
            s = s.replace("()","")
            s = s.replace("[]","")
            s = s.replace("{}","")
        if s : return False
        else : return True