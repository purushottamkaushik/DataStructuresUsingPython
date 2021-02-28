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

    def traverseInorder(self, root):

        if root is None:
            return
        self.traverseInorder(root.left)
        self.lst.append(root.info)
        self.traverseInorder(root.right)

    def listInorder(self, root):
        self.traverseInorder(root)
        return self.lst


b1 = BinaryTree()
b2 = BinaryTree()
root1 = None
root2 = None

for ele in [10, 20, 30, 40, 50, 60]:
    root1 = b1.build(root1, ele)

for ele in [10 , 20, 30, 40, 50, 60]:
    root2 = b2.build(root2, ele)

l1 = b1.listInorder(root1)
l2 = b2.listInorder(root2)

identical = True

if len(l1) == len(l2):
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            print("Demo")
            identical = False
            break
else:
    identical = False

if identical:
    print("identical")
else:
    print("not identical ")
