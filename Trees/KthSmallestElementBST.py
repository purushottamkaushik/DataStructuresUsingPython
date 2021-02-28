# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def __init__(self):
#         self.smallest = []
#
#     def kthSmallest(self, root: TreeNode, k: int) -> int:
#         lst = []
#
#         def inorder(root):
#             if root:
#                 inorder(root.left)
#                 if root.val is not None:
#                     lst.append(root.val)
#                 inorder(root.right)
#
#         inorder(root)
#         return lst[k - 1]































































