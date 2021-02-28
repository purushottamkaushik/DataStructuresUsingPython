class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None


import sys

best = - sys.maxsize -1
bestleafnode = None
currentsum = 0


# def bestsum(root, currentsum):
#     global best
#     # base case 1 : if root is null
#     if root is None:
#         return None
#     # update current sum value
#     currentsum += root.info
#     print("Current sum is " , currentsum)
#     # Base case 2 : if the current node is leaf node then check currentsum > bestsum
#
#     if root.left is None and root.right is None:
#         if currentsum > best:
#
#             best = currentsum  # update the bestsum
#             print("Best is " , best)
#             bestleafnode = root  # update the best leaf node
#
#     bestsum(root.left, currentsum)
#     bestsum(root.right, currentsum)



def bestsum(root,currentsum):
    global best
    # if node is null
    if root is None:
        return None

    # node is not null
    currentsum +=root.info

    # leaf node
    if root.left is None and root.right is None:
        if currentsum > best:
            best = currentsum
            bestleafnode = root

    # else  recursive case

    bestsum(root.left,currentsum)
    bestsum(root.right,currentsum)





root = Node(2)
root.left = Node(3)
root.right = Node(4)
root.right.right = Node(10)
root.left.left = Node(-4)
root.left.right = Node(-100)
root.left.left.left = Node(6)
root.left.left.right = Node(10)

bestsum(root, currentsum)

print(best)
print(bestleafnode)
