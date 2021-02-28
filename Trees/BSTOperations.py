class Node:

    def __init__(self,data):
        self.info = data
        self.left = None
        self.right = None


class BST:
    def buildbst(self,root,ele):
        if root is None:
            return Node(ele)
        elif ele < root.info :
            root.left = self.buildbst(root.left,ele)
        else:
            root.right = self.buildbst(root.right,ele)

        return root

    def displayinorder(self,root):
        if root is None:
            return
        else:
            # self.count +=1;
            self.displayinorder(root.left)
            print(root.info,end=" ")
            self.displayinorder(root.right)




    def search(self,root,element):
        if root is None or root.info == element:
            return root
        if root.info > element:
            return self.search(root.left,element)
        return self.search(root.right,element)

    def findmin(self,root):
        current = root
        while current.left is not None:
            current = current.left
        return current.info


    def findmax(self,root):
        """
        From the intitution we know that maximum value
        exists only in the right subtree
        :param root:
        :return:
        """
        current = root
        while current.right is not None :
            current = current.right
        return current.info

if __name__=="__main__":
    root = None
    b = BST()

    for ele in [10,5,25,2,7,30]:
        root = b.buildbst(root,ele)

    b.displayinorder(root)
    print()
    # print("Number of nodes in the tree " , b.count)
    ele = 70
    res =  b.search(root,ele)
    if res is None:
        print("Element {} not Found".format(ele))
    else:
        print("Element {} found in the BST ".format(ele))

    print("Minimum element is  " ,b.findmin(root))
    print("Maximum element is  " , b.findmax(root))