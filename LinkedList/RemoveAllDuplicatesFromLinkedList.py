
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def deleteDuplicates(self, head: ListNode) -> ListNode:
#
#         dummy = ListNode(0)
#         dummy.next = head
#
#         prev = dummy
#         current = head
#
#         while current != None:
#             while current.next != None and prev.next.val == current.next.val:
#                 current = current.next
#
#             if prev.next != current:
#                 prev.next = current.next
#             else:
#                 prev = current
#
#             current = current.next
#
#         return dummy.next


