class Node:
    def __init__(self,info):
        self.info = info
        self.left = None
        self.right = None


class BST:

    def build(self,root,ele):
        if root is None:
            return Node(ele)
        if ele < root.info:
            root.left = self.build(root.left,ele)
        else:
            root.right =self.build(root.right,ele)

        return root

    def inorder_Iterative(self,root):
        if root is None:
            return
        stack = []
        stack.append(root)

        while stack:
            current = stack.pop()
            print(current.info ,end=" ")

            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)


if __name__=="__main__":
    b = BST()
    root = None
    for ele in [10,5,2,7,25,30]:
        root = b.build(root,ele)
    print("Inorder Iterative ")
    b.inorder_Iterative(root)
