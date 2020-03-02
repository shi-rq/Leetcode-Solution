'''
Given an array of size n, find the majority element. The majority element is the element that appears more than [ n/2 ] times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
'''


# 1 Sort()
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        compare = nums[0]
        count = 1
        edge = len(nums) / 2
        for i in nums[1:]:
            if i != compare:
                compare = i
                count = 1
            else : count += 1
            if count > edge : return i
        return nums[0]  # single element


# 2 Hash
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for i in nums:
            if count.__contains__(i) : count[i] += 1
            else : count[i] = 1
        edge = len(nums) / 2
        for i in count.items():
            if i[1] > edge : return i[0]


# 3 Boyer-Moore Voting Algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        count = 1
        for i in nums[1:]:
            if i == candidate : count += 1
            else : count -= 1
            if count == 0:
                candidate = i
                count = 1
        return candidate