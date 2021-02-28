class Node:
    def __init__(self,data):
        self.info = data
        self.next = None

class LinkedListV2:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("List is empty")
        temp = self.head
        while temp:
            print(temp.info,end=" ")
            temp = temp.next
        print()

    def insertAtEnd(self,data):
        self.data = Node(data)
        if self.head is None:
            self.head = self.data
        else:
            currNode  = self.head # head refers to the first node
            while currNode.next is not None:
                currNode = currNode.next
            currNode.next = self.data



    def insertAtBeg(self,item):
        node = Node(item)
        if self.head is None:
            self.head = node

        node.next = self.head
        self.head = node


    def rotate(self,k):
        if self.head is None:
            return
        pos = self.head

        for i in range(k):
            pos = pos.next

        temp = self.head
        while pos.next is not None:
            temp = temp.next
            pos = pos.next

        Next = temp.next
        temp.next = None
        pos.next = self.head
        self.head = Next

        return  self.head



if __name__=="__main__":
    list = LinkedListV2()
    list.insertAtEnd(1)
    list.insertAtEnd(2) # Insert at the end
    list.insertAtEnd(3)
    list.insertAtEnd(4)
    list.insertAtEnd(5)
    list.display()
    rotated = list.rotate(3)

    while rotated:
        print(rotated.info , sep=" " ,end= " ")
        rotated = rotated.next
