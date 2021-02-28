class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None


mydict = dict()


def traversevertical(root, mydict, dist):
    if root is None:
        return
    try:
        mydict[dist].append(root.info)
    except:
        mydict[dist] = [root.info]

    traversevertical(root.left, mydict, dist - 1)
    traversevertical(root.right, mydict, dist + 1)


def printvertical():
    for item in sorted(mydict.items()):
        for ele in item[1]:
            print(ele)


        # for ele in item:
        #     print(ele)


dist = 0
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(4)
root.right.left.left = Node(6)
root.right.left.right = Node(7)
root.right.right = Node(5)
traversevertical(root, mydict, dist)
printvertical()