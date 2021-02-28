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

    def postorder_recursive(self,root):
        if root is None:
            return
        self.postorder_recursive(root.left)
        self.postorder_recursive(root.right)
        print(root.info,end=" ")

    def postorder_iterativetwostack(self,root):
        recstack = []
        result = []

        recstack.append(root)
        while recstack:
            current = recstack.pop()
            result.append(current.info)

            if current.left:
                recstack.append(current.left)

            if current.right:
                recstack.append(current.right)

        while result:
            print(result.pop())




if __name__=="__main__":
    b = BST()
    root = None
    for ele in [10,5,2,7,25,30]:
        root = b.build(root,ele)
    print("Postorder Recursive  ")
    b.postorder_recursive(root)
    print("\nPostOrder Iterative")
    # print(b.postorder_iterativetwostack(root))
    order = b.postorder_iterativetwostack(root)
    # print(list(reversed(order)))
    print("Using Single stack ")


