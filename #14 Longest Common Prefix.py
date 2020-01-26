'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
'''


# 1 Basic Method
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == [] : return ""
        prefix = ""
        count = 0
        minlength = len(strs[0])
        for i in strs[1:]:
            if len(i) < minlength : minlength = len(i)
        while(1):
            if count == minlength : break
            flag = True
            sample = strs[0][count]
            for i in strs[1:]:
                if sample != i[count] : flag = False
            if flag == False : break
            prefix += sample
            count += 1
        return prefix


# 2 Simplified version
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == [] : return ""
        minl = len(strs[0])
        for i in strs[1:] :
            if len(i) < minl : minl = len(i)
        prefix = strs[0][:minl]
        for n in range(minl):
            for i in strs[1:]:
                if i[n] != prefix[n]:
                    return prefix[:n]
        return prefix  # in case inputs like [""]