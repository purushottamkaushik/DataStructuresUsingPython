class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.lst = []

    def build(self, root, ele):
        if root is None:
            return Node(ele)
        if ele < root.info:
            root.left = self.build(root.left, ele)
        else:
            root.right = self.build(root.right, ele)

        return root

    def levelorderTraversal(self, root):
        if root is None:
            return
        stack = []

        stack.append(root)

        while stack:
            current = stack.pop(0)
            print(current.info ,end=" ")

            if current.left:
                stack.append(current.left)

            if current.right:
                stack.append(current.right)


if __name__=="__main__":
    b = BinaryTree()
    root = None
    for ele in [10,20,30,40,50,60,70,80,90,100]:
        root = b.build(root,ele)



    b.levelorderTraversal(root)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def levelOrder(self, root: TreeNode) -> List[List[int]]:
#         resultstack = []
#
#         if root is None:
#             resultstack.append()
#         stack = []
#         finallist = []
#         stack.append(root)
#         while stack:
#             current = stack.pop(0)
#             if current:
#                 resultstack.append(current.val)
#             else:
#                 resultstack.append(current)
#
#             if current and current.left:
#                 stack.append(current.left)
#             else:
#                 stack.append(None)
#
#             if current and current.right:
#                 stack.append(current.right)
#             else:
#                 stack.append(None)
#         finallist.append(resultstack)
#
#         return finallist
