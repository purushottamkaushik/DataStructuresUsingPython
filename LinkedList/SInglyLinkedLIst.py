class Node :
    def __init__(self,data):
        self.info = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self,data):
        print("IAT---BEG  " , data)
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def display(self):
        print("Printing LinkedList Elements ")
        if self.head == None:
            print("List is Empty")
            return
        current = self.head
        while current:
            print(current.info)
            current = current.next

    def insertAtEnd(self,data):
        print("Insert at the end " , data)
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return

        current = self.head
        while current.next is not None:
            current = current.next

        #
        # print("Printing current " ,current)
        # print("Printing current.next " ,current.next)
        current.next = newNode

    def insertAtPos(self,data,pos):
        newNode = Node(data)

        # If position is 1 then insert at the begiining
        if pos ==1 :
            newNode.next = self.head
            self.head = newNode
            return

        current = self.head

        while pos > 2 and current.next is not None:
            current = current.next
            pos =-1

        if current.next is None:
            print("Position doesnt exist ")
        else:
            newNode.next = current.next
            current.next = newNode


    def deleteNode(self,data):
        if self.head is None:
            print("List is Empty ")
            return

        if self.head.info == data:
            temp = self.head
            self.head = temp.next
            del temp

            return

        current = self.head
        prev = None

        while current.next !=None:
            prev = current
            current = current.next

            if current.info == data:
                temp = current
                prev.next = temp.next
                temp = None

        print(data , "Element not Found ")

    def search(self,ele):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        while current:
            if current.info == ele:
                print("ELEment found")
                return
            current = current.next

        print("Element not found")

if __name__=="__main__":
    ll = LinkedList()
    ll.display()
    ll.insertAtBeginning(2)
    ll.insertAtBeginning(1)
    ll.display()
    ll.insertAtEnd(3)
    ll.display()

    ll.insertAtPos(10,4)
    ll.display()
    ll.deleteNode(30)
    ll.display()
    ll.search(101)
