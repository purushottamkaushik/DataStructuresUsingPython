class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("Empty List")
            return
        temp = self.head
        while temp:
            print(temp.data )
            temp = temp.next

    def insertAtEnd(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = node

    def AlternativeSplit(self):
        currentNode = self.head
        temp1 = None
        temp2 = None

        while currentNode:
            newnode = currentNode
            currentNode = currentNode.next
            newnode.next = temp1
            temp1 = newnode
            while currentNode:
                newnode1 = currentNode
                currentNode = currentNode.next
                newnode1.next = temp2
                temp2 = newnode1
                break

        return temp1,temp2


if __name__ == "__main__":
    lst = LinkedList()
    lst.display()            
    lst.insertAtEnd(1)
    lst.insertAtEnd(2)
    lst.insertAtEnd(3)
    lst.insertAtEnd(4)
    lst.insertAtEnd(5)
    lst.display()

    lst1 ,lst2 = lst.AlternativeSplit()

    print("Printing list 1")
    while lst1:
        print(lst1.data,sep="###")
        lst1 = lst1.next

    print("Printing list 2")

    while lst2:
        print(lst2.data , sep="@@@")
        lst2 = lst2.next

