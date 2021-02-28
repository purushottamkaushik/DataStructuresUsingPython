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
#
# def searchbst(root, value):
#     if root is None or root.info == value:
#         return root
#
#     if value < root.info:
#         return searchbst(root.left,value)
#     else:
#         return searchbst(root.right,value)












def searchbst(root,val):

    while root !=None and root.info != val:
        if root.info > val:
            root = root.left
        else:
            root = root.right

    return root

root = Node(4)
root.left = Node(2)
root.left.left = Node(1)
root.left.right = Node(3)
root.right = Node(7)

inorder(root)
print()
ele = 2
found = searchbst(root, ele)


print("Type found " , type(found))
inorder(found)