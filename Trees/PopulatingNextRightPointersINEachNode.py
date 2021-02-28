
class Node:
    def __init__(self,info):
        self.info = info
        self.left = None
        self.right = None
        self.rightlevel = None


class Solution:

    def populate(self,root):
        q = [root, None]


        while q:
            element = q.pop(0)

            if element is None:
                if q:
                    q.append(element)
            else:
                element.rightlevel = q[0]
                if element.left:
                    q.append(element.left)
                if element.right:
                    q.append(element.right)

        return root





    def printinorder(self,root):
        if root is None:
            return root
        self.printinorder(root.left)
        if root.rightlevel is not None:
            print("Printing root value " , root.info , " rootright :  ", root.rightlevel.info)
        else:
            print("Printing root value 1 " , root.info , " rootright :  ", root.rightlevel)

        self.printinorder(root.right)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

p =  Solution()
p.populate(root)

p.printinorder(root)


