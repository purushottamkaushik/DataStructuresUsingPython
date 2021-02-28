class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.info, end=" ")
    inorder(root.right)



depth = []

def findmaxdepth(root,currentdepth):

    # global max_depth

    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 0
    else:
        currentdepth +=1
        findmaxdepth(root.left,currentdepth)
        findmaxdepth(root.right,currentdepth)
        depth.append(currentdepth)

def findmaxdepth2(root):
    if root is None:
        return 0
    return 1 + max(findmaxdepth2(root.left) , findmaxdepth2(root.right))


root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)
root.right.right.right = Node(17)

findmaxdepth(root,currentdepth=1)
print("Max Depth is " , max(depth))
print("Another recursive method " , findmaxdepth2(root) )
