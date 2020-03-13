'''
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# 1 Iteration
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head: return None
        lh = head
        mid = lh.next
        lh.next = None
        while mid:
            rh = mid.next
            mid.next = lh
            lh = mid
            mid = rh
        return lh


# 2 Recursion
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head: return None
        elif not head.next: return head
        else:
            start = self.reverseList(head.next)
            head.next.next = head
            head.next = None
            return start