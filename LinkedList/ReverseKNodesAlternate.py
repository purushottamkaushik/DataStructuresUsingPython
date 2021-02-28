class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            return
        temp = self.head
        while temp:
            print(temp.data, sep=" ", end=" ")
            temp = temp.next

    def insertAtEnd(self, data):
        self.data = Node(data)
        currNode = self.head  # head refers to the first node

        if self.head is None:
            self.head = self.data
        else:
            while currNode.next is not None:
                currNode = currNode.next
            currNode.next = self.data


def reverse(head, k):
    current = head
    prev = None
    count = 0
    while current is not None and count < k:
        Next = current.next
        current.next = prev
        prev = current
        current = Next
        count += 1

    if head is not None:
        head.next = current


    # t = prev
    # while t:
    #     print(t.data)
    #     t = t.next

    count = 0
    while count < k - 1 and current is not None:
        current = current.next
        count += 1

    if current is not None:
        current.next = reverse(current.next, k)
    return prev


if __name__ == "__main__":
    lst = LinkedList()
    n,k = [ int(i )for i in input().split(" ")]
     
    # print("N value ", n)
    # print("K values " , k)

    values = [ int(j) for j in input().split(" ")]

    for i in values:
        lst.insertAtEnd(i)


    lst.head = reverse(lst.head, 3)
    lst.display()