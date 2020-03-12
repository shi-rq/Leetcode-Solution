'''
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.
'''


# 1 Map each other
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map = {}
        for n in range(len(s)):
            if map.__contains__(s[n]):
                if map[s[n]] != t[n]: return False
            else: map[s[n]] = t[n]
        map = {}
        for m in range(len(t)):
            if map.__contains__(t[m]):
                if map[t[m]] != s[m]: return False
            else: map[t[m]] = s[m]
        return True


# 2 Map to a third part
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map = {}
        code = 0
        s_mapped = ""
        t_mapped = ""
        for i in s:
            if not map.__contains__(i):
                map[i] = code
                code += 1
            s_mapped += str(map[i])

        map = {}
        code = 0
        for j in t:
            if not map.__contains__(j):
                map[j] = code
                code += 1
            t_mapped += str(map[j])
        if s_mapped == t_mapped: return True
        else: return False