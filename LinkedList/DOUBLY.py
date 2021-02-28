
class DNode:
    def __init__(self,data):
        self.prev = None
        self.info = data
        self.next = None

class DLinkedList:
    def __init__(self):
        self.head = None
        print("Doubly linkedlist created ")

    def display(self):
        if self.head is None:
            print("Empty list ")
            return
        temp = self.head
        while temp:
            print(temp.info)
            temp = temp.next


    def insertAtEnd(self,data):
        node = DNode(data)

        if self.head is None:
            self.head = node
            return

        temp = self.head

        while temp.next is not None : # it will run after the second node
            temp = temp.next
        # print("Printing temproray data " , temp)

        temp.next = node
        node.prev = temp
        node.next = None


    def insertAtBeg(self,item):
        self.node = DNode(item)

        if self.head is None:
            self.head = self.node
            return

        self.node.next = self.head # node pointing to node pointed by head
        self.head.prev = self.node # back from second node to first
        self.head = self.node # head contains the current node


    def insertAfterElement(self,element,item):
        self.temp = DNode(item)
        self.p = self.head

        while self.p is not None:
            if self.p.info == element:
                self.temp.prev = self.p
                self.temp.next = self.p.next
                if self.p.next.prev is not None:
                    self.p.next.prev = self.temp
                self.p.next = self.temp
                return # from the if loop
            self.p = self.p.next # p points to the next node 

    def delete(self,item):
        # if the list is empty
        if self.head is None:
            print("Empty list")
            return
        # if only one item is there
        if self.head.next is None:
            if self.head.info == item:
                temp = self.head
                self.head = self.head.next
                return
            else:
                print("Element " , item , " doesnt exist in the list ")

         # Deletion of the first element
        if self.head.info == item:
            temp = self.head
            temp.prev = self.head
            self.head = self.head.next
            # self.head.prev = None
            print("Deletion From first element " , item)
            return

        # deleting the element in between
        # self.p = None
        curr = self.head

        while curr.next is not None:

            if curr.info == item:
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
                return

            curr = curr.next

        # deleting the last element
        self.p = None
        self.temp = self.head
        while self.temp.next:
            self.p = self.temp
            self.temp = self.temp.next

        # self.p.next = None
        self.temp.prev.next = None
        # print("Printing self.temp " , self.temp)











if __name__=="__main__":
    lst = DLinkedList()
    # lst.display()
    lst.insertAtEnd(2)
    lst.insertAtEnd(3)
    lst.insertAtEnd(4)
    lst.insertAtEnd(5)
    lst.display()
    print("----------------")
    lst.insertAtBeg(1)
    lst.insertAtBeg(0)

    lst.display()
    print("================================================")
    lst.insertAfterElement(4,6)
    lst.delete(5)
    lst.display()
