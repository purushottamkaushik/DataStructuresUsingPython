class Node:
    def __init__(self,data):
        self.info = data
        self.left = None
        self.right = None

# def childrensum(root):
#     if root is None:
#         return
#     if root.left is None :
#         return
#
#     if root.right is None:
#         return
#
#     if root.right is not None or root.left is not None:
#         if root.left.info + root.right.info != root.info:
#             return False
#         else:
#             return True
#
#     childrensum(root.left)
#     childrensum(root.right)



def childrensum(root):
    if root is None or (root.right is None and root.left is None):
        return True

    l = 0; r =0
    if root.left is not None:
        l = root.left.info
    if root.right is not None:
        r = root.right.info

    if root.info == l + r and childrensum(root.left) and childrensum(root.right):
        return True
    else:
        return False











root = Node(20)
root.left = Node(12)
root.left.left = Node(6)
root.left.right = Node(6)
root.right = Node(8)
root.right.left = Node(3)
root.right.right = Node(5)
root.right.right.left = Node(5)

print(childrensum(root))
