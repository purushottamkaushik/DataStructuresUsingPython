class Node:
    def __init__(self,info):
        self.info = info
        self.left = None
        self.right = None

def swap(left,right):

    temp = left
    left = right
    right = temp

    return left,right


def inorder(root):
    if root is None:
        return
    else:
        inorder(root.left)
        print(root.info)
        inorder(root.right)


def mirrorBinaryTree(root):
    if root is None:
        return

    mirrorBinaryTree(root.left)
    mirrorBinaryTree(root.right)
    temp = root.left
    root.left = root.right
    root.right = temp





root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.left.left.left = Node(7)
root.left.left.right = Node(8)

inorder(root)
mirrorBinaryTree(root)

print()
inorder(root)