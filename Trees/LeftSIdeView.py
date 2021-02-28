class Node:
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
            if queue[0] is not None:
                level.append(queue[0].val)

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