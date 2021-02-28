class Node:
    def __init__(self, info=2):
        self.info = info
        self.left = None
        self.right = None

cnt = 0

def count(root):
    global cnt
    if root is None:
        return 0
    count(root.left)
    cnt += 1
    count(root.right)


diam = 0
def compute_height(root):
    global diam
    if root is None:
        return -1

    l = compute_height(root.left)
    r = compute_height(root.right)

    # daim = max(diam, 2 + l + r)
    return (1 + max(l, r))


def compute_d(root):
    global diam
    if root is None:
        return -1

    l = compute_d(root.left)
    r = compute_d(root.right)

    diam = max(diam, 2 + l + r)
    return 1 + max(l,r)



root = Node()
root.left = Node()
root.left.left = Node()
root.right = Node()
root.right.left = Node()
root.right.left.left = Node()
root.right.left.right = Node()
root.right.left.right.left = Node()
root.right.left.right.right = Node()
root.right.right = Node()
root.right.right.left = Node()
root.right.right.right = Node()
root.right.right.right.right = Node()

count(root)
print(cnt)

print(compute_height(root))
compute_d(root)
print(diam)











######
#
#
# import sys
#
# ans = -sys.maxsize - 1
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
# def height(ptr):
#     global ans
#     if ptr is None:
#         return 0
#
#     lheight = height(ptr.left)
#     rheight = height(ptr.right)
#     ans = max(ans, 1 + lheight + rheight)
#     if lheight > rheight:
#         return 1 + lheight
#     else:
#         return 1 + rheight
#
#
# def getDiameter(root):
#     if root is None:
#         return 0
#     h = height(root)
#
#
# if __name__ == '__main__':
#     root = None
#     root = node(10)
#     root.left = node(20)
#     root.right = node(30)
#     root.left.left = node(40)
#     root.left.right = node(50)
#     getDiameter(root)
#     print(ans)
