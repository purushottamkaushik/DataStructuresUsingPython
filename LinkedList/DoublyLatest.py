class Node:
    def __init__(self,info):
        self.info = info
        self.prev = None
        self.next = None


class DLinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self,data):
        newNode = Node(data)

        # EMPTY LIST
        if self.head is None:
            self.head = newNode
            return
        else:
            # NON EMPTY LIST
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode


    def display(self):
        if self.head is None:
            print("List is Empty")
            return
        current = self.head
        while current:
            print(current.info)
            current = current.next

    def insertAtEnd(self,data):
        print("InsertAtthe end  " , data)
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return
        else:
            current =self.head
            while current.next != None:
                current = current.next
            # print("Printing current.next " ,current.next)
            current.next = newNode
            newNode.prev = current
            # print("Printing current.next " ,current.next)

if __name__=="__main__":
    ll = DLinkedList()
    ll.display()
    ll.insertAtBeginning(3)
    ll.insertAtBeginning(2)
    ll.display()
    ll.insertAtEnd(20)
    ll.insertAtEnd(30)
    ll.insertAtEnd(40)
    ll.display()
