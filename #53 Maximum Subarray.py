'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum
and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is
more subtle.
'''


# 1 o(n^2), Simple search
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]s
        len0 = len(nums)
        for n in range(0, len0):
            for m in range(n, len0):
                sum0 = sum(nums[n: m+1])
                if sum0 > maxsum : maxsum = sum0
        return maxsum


# 2 o(n), Expire negatives
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        sum0 = 0
        for i in nums:
            sum0 += i
            maxsum = max(maxsum, sum0)
            if sum0 < 0 : sum0 = 0
        return maxsum


# 3 Recursion