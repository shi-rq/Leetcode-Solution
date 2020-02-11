'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
'''


# 1 Sort()
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums2 += nums1[0: m]
        nums2.sort()
        for p in range(m+n):
            nums1[p] = nums2[p]


# 2 Sort in an extra array
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p, q = 0, 0
        merge = []
        while p < m and q < n:
            if nums1[p] < nums2[q]:
                merge.append(nums1[p])
                p += 1
            else:
                merge.append(nums2[q])
                q += 1
        if p < m : merge += nums1[p: m]
        else : merge += nums2[q: n]
        for r in range(m+n):
            nums1[r] = merge[r]