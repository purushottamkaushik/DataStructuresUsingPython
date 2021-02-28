# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:

        if root is None:
            return 0

        level = [root]
        finallist = [root.val]

        while level:
            nextlevel = []
            toadd = []

            for element in level:
                if element.left:
                    nextlevel.append(element.left)
                if element.right:
                    nextlevel.append(element.right)

            for element in nextlevel:
                toadd.append(element.val)

            if len(toadd) > 0:
                finallist.append(sum(toadd) / len(toadd))

            level = nextlevel

        return finallist


