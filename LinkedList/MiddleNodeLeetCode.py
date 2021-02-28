# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def middleNode(self, head: ListNode) -> ListNode:
#         slow = head
#         fast = head
#
#         count = 0
#         temp = head
#         while temp:
#             count += 1
#             temp = temp.next
#
#         iseven = False
#         if count % 2 == 0: isEven = True
#
#         if iseven:
#             while fast and fast.next is not None:
#                 slow = slow.next
#                 fast = fast.next.next
#
#             return slow.next
#         else:
#             while fast and fast.next is not None:
#                 slow = slow.next
#                 fast = fast.next.next
#             return slow
#

