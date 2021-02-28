class Node:

    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.cnt = 0

    def count(self, root):

        if root is None:
            return

        self.count(root.left)

        if root.left is None and root.right is None:
            self.cnt += 1

        self.count(root.right)


t = Tree()
# root = None
root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.right = Node(3)
root.right.right= Node(5)
root.right.right.left = Node(6)
root.right.right.right = Node(7)
root.right.left = Node(11)

print("Before counting ", t.cnt)
t.count(root)

print("After counting ", t.cnt)

#


#
# class node:
#
#     def __init__(self, info):
#         self.info = info
#         self.left = None
#         self.right = None
#
#
# def insert(ptr, key):
#     if (ptr is None):
#         ptr = node(key)
#     elif (key <= ptr.info):
#         ptr.left = insert(ptr.left, key)
#     elif (key > ptr.info):
#         ptr.right = insert(ptr.right, key)
#     return ptr
#
#
# def getLeafcount(root):
#     if (root == None):
#         return 0
#     if (root.left == None and root.right == None):
#         return 1
#
#     return getLeafcount(root.left) + getLeafcount(root.right)
#
#
# if __name__ == '__main__':
#     root = None
#     root = insert(root, 10)
#     root = insert(root, 5)
#     root = insert(root, 15)
#     root = insert(root, 30)
#     print(getLeafcount(root))
