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


def similarleaf(root,root1):

    list1 = []
    list2 = []

    def recursive(root,num):
        if root is None:
            return root
        recursive(root.left,num)

        if root.left is None and root.right is None and num==1:
            list1.append(root.info)

        if root.left is None and root.right is None and num==2:
            list2.append(root.info)

        recursive(root.right,num)

    recursive(root,1)
    recursive(root1,2)
    print(list1)

    print(list2)
    return list1 == list2







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



root1 = Node(5)
root1.left = Node(4)
root1.right = Node(8)
root1.left.left = Node(11)
root1.left.left.left = Node(7)
root1.left.left.right = Node(2)
root1.right.left = Node(13)
root1.right.right = Node(4)
root1.right.right.right = Node(1)

inorder(root)
print()
inorder(root1)
print()
print(similarleaf(root, root1))

