class Node:
    def __init__(self,info):
        self.info = info
        self.left = None
        self.right = None

class BST:

    def buildbst(self,root,ele):

        if root is None:
            return Node(ele)
        if ele < root.info:
            root.left = self.buildbst(root.left,ele)
        else:
            root.right =  self.buildbst(root.right,ele)

        return root

    def preorder(self,root):
        if root is None:
            return
        print(root.info , end=" ")
        self.preorder(root.left)
        self.preorder(root.right)

    def preorderIterative(self,root):
        if root is None: # If the tree is Empty return None
            return
        stack = [] # stack to hold nodes in the of the tree for traversal
        # creating an empty stack and appending root to it....
        stack.append(root) # if not empty append root to the stack


        while stack:
            x =stack.pop() # popping the node
            print(x.info ,end=" ") # printing the data of the node

            if x.right:
                stack.append(x.right)
                # becoz we want it to be after the left child of the tree
            if x.left:
                stack.append(x.left)





if __name__=="__main__":
    b = BST()
    root = None
    for ele in [10,5,15,20,25,30,6]:
        root = b.buildbst(root,ele)

    print("Printing IN preorder ")
    b.preorder(root)
    print("\nPreorder Iterative")
    b.preorderIterative(root)