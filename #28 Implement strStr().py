'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr()
and Java's indexOf().
'''


# 1 ????
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try : return haystack.index(needle)
        except ValueError : return -1


# 2 BruteForce
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i, j , start = 0, 0, 1
        while i < len(haystack) and j < len(needle):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                i = start
                j = 0
                start += 1
        if j == len(needle) : return i-j
        else : return -1


# 3 Sunday
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i, j , start = 0, 0, 1
        while i < len(haystack) and j < len(needle):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            elif not haystack[i] in needle:
                i += 1
                j = 0
                start = i + 1
            else:
                i = start
                j = 0
                start += 1
        if j == len(needle) : return i-j
        else : return -1


# 4 Rabin-Karp
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_needle = len(needle)
        len_haystack = len(haystack)
        needle_hash = hash(needle)
        haystack_hash = []
        for n in range(len_haystack - len_needle + 1):
            haystack_hash.append(hash(haystack[n: n+len_needle]))
        for n in range(len(haystack_hash)):
            if needle_hash == haystack_hash[n] : return n
        return -1


# 5 KMP
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        fall = [-1, 0]
        lh, rh = 0, 2
        while rh < len(needle):
            if needle[lh] == needle[rh - 1]:
                lh += 1
                rh += 1
                fall.append(lh)
            elif lh > 0:
                lh = fall[lh]
            else:
                fall.append(0)
                rh += 1

        i, j = 0, 0
        while i < len(haystack) and j < len(needle):
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = fall[j]
        if j == len(needle):
            return i - j
        else:
            return -1


# 6 Z-algorithm o(n^2)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle : return 0
        n_h = needle + haystack
        for i in range(len(needle), len(haystack)+1):
            match = 0
            while i + match < len(n_h) and n_h[match] == n_h[i+match]:
                match += 1
            if match >= len(needle) : return i - len(needle)
        return -1


# 7 Z-algorithm o(n) (部分例子有bug，还在研究)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle : return 0
        n_h = needle + haystack
        len0 = len(n_h)
        match = [0 for n in range(len0)]
        lh, rh = 0, 0
        for i in range(1, len0):
            if i <= rh:
                match[i] = min(match[i-lh], rh-i+1)
            else:
                while i + match[i] < len0 and n_h[match[i]] == n_h[i+match[i]]:
                    match[i] += 1
                if i + match[i] - 1 > rh:
                    lh = i
                    rh = i + match[i] - 1
        for n in range(len(needle), len(match)):
            if match[n] >= len(needle) : return n - len(needle)
        return -1