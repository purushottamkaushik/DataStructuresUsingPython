class Node:
    def __init__(self, info):
        self.info = info
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode  # assigning the newnode to the head
            self.head.next = self.head  # for circular loop

            return
        else:
            current = self.head

            while current.next is not self.head:
                current = current.next
            # print(current)
            current.next = newNode
            newNode.next = self.head
            self.head = newNode

    def insertAtEnd(self, data):
        print("Insertion at the end ", data)
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            newNode.next = self.head
            return
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = newNode
            newNode.next = self.head

    def display(self):
        if self.head is None:
            print("Empty List")
            return
        current = self.head

        while current.next != self.head:
            print(current.info, sep=" ")
            current = current.next
        print(current.info)
        # print(current.next.info)

    #
    # def deleteNode(self,element):
    #     print("After deleting node ",element)
    #     if self.head is None:
    #         print("List is Empty")
    #         return
    #     elif self.head.info == element:
    #         # deleting the first element of the list
    #         current = self.head
    #         while current.next != self.head :
    #             current = current.next
    #         current.next = self.head.next
    #         self.head = self.head.next
    #         return
    #     else :
    #         current =self.head
    #         prev = None
    #         while current.next != self.head:
    #             prev = current
    #             current = current.next
    #
    #             if current.info == element:
    #                 # print("Entering if in while")
    #                 temp = current
    #                 # print("Printing temp.info " ,temp.info)
    #                 prev.next = temp.next
    #                 # print("prev.next.info " , prev.next.info)
    #                 temp = None
    #                 return
    #
    #     print("Printing current.next " , current.next.info)
    #     print("Printing self.head " ,self.head.info)
    #     print("Element not found")

    def deleteNode(self, element):
        print("After deleting node ", element)
        if self.head is None:
            print("List is Empty")
            return
        elif self.head.info == element:
            # deleting the first element of the list
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
            return
        else:
            current = self.head
            while current.next != self.head:
                if current.next.info == element:
                    current.next = current.next.next
                    return
                current = current.next

        print("Printing current.next ", current.next.info)
        print("Printing self.head ", self.head.info)
        print("Element not found")


if __name__ == "__main__":
    ll = CircularLinkedList()
    ll.insertAtBeginning(10)
    ll.insertAtBeginning(11)
    ll.insertAtBeginning(12)
    ll.display()
    ll.insertAtEnd(20)
    ll.insertAtEnd(30)
    ll.display()
    ll.deleteNode(200)
    ll.display()
    ll.insertAtBeginning(1)
    ll.insertAtEnd(2000)
    ll.display()
    ll.deleteNode(2000)
    ll.display()
