class Node:
    def __init__(self,info):
        self.info = info
        self.left = None
        self.right = None

class BST:
    cnt = 0
    def build(self,root,ele):
        if root is None:
            return Node(ele)
        if ele < root.info:
            root.left = self.build(root.left,ele)
        else:
            root.right = self.build(root.right,ele)

        return root

    def count(self,root):
        if root is None:
            return
        self.count(root.left)
        if True:
            self.cnt +=1
        self.count(root.right)
        return self.cnt


if __name__=="__main__":
    b = BST()
    root = None
    for ele in [10,12,6,8,9,10,2]:
        root = b.build(root,ele)

    print("The number of nodes in the tree are " , b.count(root))





# import sys


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
# def countNodes(root):
#     if root == None:
#         return 0
#     return (1 + countNodes(root.left) + countNodes(root.right))
#
#
# if __name__ == '__main__':
#     root = None
#     root = insert(root, 10)
#     root = insert(root, 20)
#     root = insert(root, 5)
#     root = insert(root, 30)
#     print(countNodes(root))
