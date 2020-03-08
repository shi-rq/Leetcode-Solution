'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
'''


# 1 Recursion
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        elif len(nums) == 1: return nums[0]
        elif len(nums) == 2: return max(nums)
        else:
            return max(self.rob(nums[:-2]) + nums[-1], self.rob(nums[:-1]))


# 2 Iteration (7.11%)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        left = nums[0]
        if len(nums) == 1: return left
        mid = max(nums[0], nums[1])
        if len(nums) == 2: return mid
        for i in nums[2:]:
            right = max(left + i, mid)
            left = mid
            mid = right
        return right
# Improved (99.91%)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        nums[1] = max(nums[0], nums[1])
        if len(nums) == 2: return nums[1]
        for n in range(2, len(nums)):
            nums[n] = max(nums[n-2] + nums[n], nums[n-1])
        return nums[-1]