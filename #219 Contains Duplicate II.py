'''
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
'''


# 1 Basic method
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for n in range(len(nums) - 1):
            for i in nums[n+1: n+k+1]:
                if nums[n] == i: return True
        return False


# 2 Hash
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        location = {}
        for n in range(len(nums)):
            if location.__contains__(nums[n]):
                if n - location[nums[n]] <= k: return True
                else: location[nums[n]] = n
            else: location[nums[n]] = n
        return False