'''

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
'''


# 1 Basic method
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for n in range(len(nums)):
            if nums[n] in nums[n+1:]: return True
        return False


# 2 Hash
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        appeared = {}
        for i in nums:
            if appeared.__contains__(i): return True
            else: appeared[i] = None
        return False

# 3 Sort()
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        last = None
        for i in nums:
            if i == last: return True
            last = i
        return False