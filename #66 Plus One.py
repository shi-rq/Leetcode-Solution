'''
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array
contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
'''


# 1 Add digit by digit
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [0] + digits
        len0 = len(digits)
        for n in range(len0):
            digits[len0-1-n] += 1
            if digits[len0-1-n] == 10 : digits[len0-1-n] = 0
            else : break
        if digits[0] == 0 : digits.pop(0)
        return digits


# 2 transfer into integer, and then add
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        result = []
        for i in str(digits):
            if i >= "0" and i <= "9" : num += i
        num = str(int(num) + 1)
        for i in num:
            result.append(int(i))
        return result