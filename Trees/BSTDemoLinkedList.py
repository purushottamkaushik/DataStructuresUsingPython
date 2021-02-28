class Node:
    def __init__(self,data):
        self.info = data
        self.left = None
        self.right = None


class BST:

    def buildbst(self,root,ele):
        if root is None:
            # if root is None then return Single Node with info as passed element
            return Node(ele)
        if ele < root.info:
            # if element is less than root node then build the left tree recursively
            root.left = self.buildbst(root.left,ele)
        else:
            # if element is greater than root node then build the right tree recursively
            root.right = self.buildbst(root.right,ele)

        # After the tree is completely build return the root node of the tree

        return  root

    def displayinorder(self,root):
        """
        Recursive Implementation of the Inorder Display
        :param root:
        :return:
        """
        if root is None:
            return
        self.displayinorder(root.left)
        print(root.info)
        self.displayinorder(root.right)

if __name__=="__main__":
    root = None
    b = BST()
    for ele in [10,5,25,2,7,30]:
        root = b.buildbst(root,ele)

    b.displayinorder(root)

