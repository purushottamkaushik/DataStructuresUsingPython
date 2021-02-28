class Node:
    def __init__(self,info):
        self.info = info
        self.left = None
        self.right = None


def sumtree(root):
    if root is None:
        return 0;
    if root.left is None and root.right is None:
        return root.info
    
    l = sumtree(root.left)
    r = sumtree(root.right)
    n = root.info

    root.info = l +r;
    return l + r + n;


def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.info)
    inorder(root.right)

root = Node(10)
root.left = Node(-1)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = Node(3)
root.right.left = Node(-2)

inorder(root)
sumtree(root)

print("After execution ")
inorder(root)
