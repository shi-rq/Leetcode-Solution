'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# 1 Basic method
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head : return head
        p = head
        while p.next:
            if p.val == p.next.val : p.next = p.next.next
            else : p = p.next
        return head