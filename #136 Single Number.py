'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
'''


# 1 count()
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in nums:
            if nums.count(i) == 1 : return i


# 2 Using dictionary to judge uniqueness
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        compare = {}
        for i in nums:
            if compare.__contains__(i) : del compare[i]
            else : compare[i] = None
        return compare.popitem()[0]