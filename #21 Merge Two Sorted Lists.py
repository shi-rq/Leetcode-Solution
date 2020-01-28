'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes
of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# 1 Sort while linking
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode(0)
        l3_sub = l3
        while l1 and l2:
            if l1.val < l2.val:
                l3_sub.next = l1
                l1 = l1.next
                l3_sub = l3_sub.next
            else:
                l3_sub.next = l2
                l2 = l2.next
                l3_sub = l3_sub.next
        if l1 : l3_sub.next = l1
        else : l3_sub.next = l2
        return l3.next


# 2 First sort, then link
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        nodes = []
        while l1 and l2:
            if l1.val < l2.val:
                nodes.append(l1)
                l1 = l1.next
            else:
                nodes.append(l2)
                l2 = l2.next
        if l1 : nodes.append(l1)
        else : nodes.append(l2)

        l3 = ListNode(0)
        l3_sub = l3
        for i in nodes:
            l3_sub.next = i
            l3_sub = l3_sub.next
        return l3.next