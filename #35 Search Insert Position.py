'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0
'''


# 1 o(n), Simple search
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for n in range(1,len(nums)):
            if nums[n-1] < target and nums[n] >= target : return n
        if nums[0] >= target : return 0
        else : return len(nums)


# 2 o(logn), Binary search
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[0] >= target : return 0
        if nums[len(nums)-1] < target : return len(nums)
        lh, rh = 0, len(nums) - 1
        while rh - lh != 1:
            mid = int((lh + rh) / 2)
            if nums[mid] < target : lh = mid
            else: rh = mid
        return rh