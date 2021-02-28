class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.info, end=" ")
    inorder(root.right)


def invert(root):
    if root is None:
        return
    if root.left is None and root.right is None:
        return root
    if root.left or root.right:
        temp = root.left
        root.left = root.right
        root.right = temp

    invert(root.left)
    invert(root.right)








root = Node(4)
root.left = Node(2)
root.left.left = Node(1)
root.left.right = Node(3)
root.right = Node(7)
root.right.left = Node(6)
root.right.right = Node(9)

inorder(root)
invert(root)

print("\nAfter Execution  ")
inorder(root)