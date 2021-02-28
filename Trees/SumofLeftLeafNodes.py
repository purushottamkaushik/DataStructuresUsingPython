class Node:
    def __init__(self,info):
        self.val = info
        self.left = None
        self.right = None

s = 0
def sumleft(root):
    global s

    if root is None:
        return root
    sumleft(root.left)

    if root.left is not None and root.left.left is None and root.left.right is None:
        s += root.left.val
    sumleft(root.right)

    return s
root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)

print(sumleft(root))