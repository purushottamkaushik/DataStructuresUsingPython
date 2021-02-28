class Node:

    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None


class BST:
    def buildbst(self, root, ele):
        if root is None:
            return Node(ele)
        elif ele < root.info:
            root.left = self.buildbst(root.left, ele)
        else:
            root.right = self.buildbst(root.right, ele)

        return root

    def displayinorder(self, root):
        if root is None:
            return
        else:
            # self.count +=1;
            self.displayinorder(root.left)
            print(root.info, end=" ")
            self.displayinorder(root.right)

    def lca(self, root, x, y):
        # BAse case
        if root is None:
            return None

        if root.info > x and root.info > y:
            return self.lca(root.left, x, y)
        elif root.info < x and root.info < y:
            return self.lca(root.right, x, y)
        else:
            return root.info;  # required lca


if __name__ == "__main__":
    root = None
    b = BST()

    for ele in [10, 5, 25, 2, 7, 30]:
        root = b.buildbst(root, ele)

    print(b.lca(root, 2, 7))
