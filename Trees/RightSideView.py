class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


# Solution is right but exceeds time limit
# def rightsideview(root):
#     if root is None:
#         return root
#
#     queue = [root,None]
#     level = []
#     while queue:
#         element = queue.pop(0)
#         if element:
#             level.append(element.val)
#         else:
#             level.append(None)
#
#         if element is not None:
#             if element.left:
#                 queue.append(element.left)
#             if element.right:
#                 queue.append(element.right)
#         elif queue:
#             queue.append(None)
#
#     print(level)
#     rights = []
#     for i in range(1,len(level)):
#         if level[i-1] and level[i] is None:
#             rights.append(level[i-1])
#
#     print(rights)















root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right =Node(5)
root.right.right = Node(4)

# rightsideview(root)


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root):
        queue = [root]
        level = []
        while queue:
            nextlevel = []
            if queue[-1] is not None:
                level.append(queue[-1].val)

            for i in queue:
                if i is not None and i.left:
                    nextlevel.append(i.left)
                if i is not None and i.right:
                    nextlevel.append(i.right)

            queue = nextlevel

        return level



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right =Node(5)
root.right.right = Node(4)

obj = Solution()
print(obj.rightSideView(root))