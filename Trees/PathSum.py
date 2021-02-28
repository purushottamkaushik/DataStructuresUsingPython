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


def pathsum(root, sum):
    if root is None:
        return False
    path = []

    currentsum = 0
    def recursive(root, currentsum):

        if root is None: # first root must be checked if null then return
            return
        currentsum += root.info
        if root.left is None and root.right is None:
            path.append(currentsum)
            return

        recursive(root.left, currentsum)
        recursive(root.right, currentsum)

    recursive(root, currentsum)

    return sum in path


root = Node(5)
root.left = Node(4)
root.right = Node(8)
root.left.left = Node(11)
root.left.left.left = Node(7)
root.left.left.right = Node(2)
root.right.left = Node(13)
root.right.right = Node(4)
root.right.right.right = Node(1)

# inorder(root)
print(pathsum(root, 25))
