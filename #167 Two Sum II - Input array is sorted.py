'''
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
'''


# 1 o(n^2), Basic method
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for n in range(len(numbers) - 1):
            for m in range(n+1, len(numbers)):
                if numbers[n] + numbers[m] == target : return [n+1, m+1]


# 2 o(n), Close from both sides
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lh, rh = 0, len(numbers)-1
        sum = numbers[lh] + numbers[rh]
        while(sum != target):
            if sum > target : rh -= 1
            else : lh += 1
            sum = numbers[lh] + numbers[rh]
        return [lh+1, rh+1]