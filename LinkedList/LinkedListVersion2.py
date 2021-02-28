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


    def insertAtEnd(self,data):
        self.data = Node(data)
        if self.head is None:
            self.head = self.data
        else:
            currNode  = self.head # head refers to the first node
            while currNode.next is not None:
                currNode = currNode.next
            currNode.next = self.data

    def length(self):
        count = 0
        temp = self.head
        while temp:
            count +=1
            temp = temp.next
        print("Length of the list is " , count)
        return None

    def search(self,item):
        count = 0
        temp = self.head
        while temp:
            count +=1
            if temp.info == item:
                print("Element found at " , count , " Position ")
                return
            temp = temp.next
        print("Element doesnt exist ")

    def insertAtBeg(self,item):
        node = Node(item)
        if self.head is None:
            self.head = node

        node.next = self.head
        self.head = node

    def insertaftergivenElement(self,element,data):
        temp = self.head

        while temp:
            if temp.info == element:
                node = Node(data)
                node.next = temp.next
                temp.next = node
                return
            temp = temp.next
        print("Element " , element , " doesnt exist ")

    def insertAtGivenPosition(self,data,pos):
        node = Node(data)
        if pos == 1:
            node.next = self.head
            self.head = node
            return

        temp = self.head

        while pos >2 and temp:
            temp = temp.next
            pos -=1

        node.next = temp.next
        temp.next = node


    def delete(self,item):
        if self.head is None:
            print("List is Empty")
            return
        if self.head.info == item:
            self.temp = self.head
            self.head = self.head.next
            return

        self.p = None
        currnode = self.head

        while currnode:
            if currnode.info == item:
                self.temp = self.p.next # temp points to a node
                self.p.next = self.temp.next
                return
            self.p = currnode
            currnode = currnode.next
        print("Element doesnt exist")





if __name__=="__main__":
    list = LinkedListV2()
    list.insertAtEnd(1)
    list.insertAtEnd(2) # Insert at the end
    list.display()
    list.insertAtEnd(3)
    print("--------------------")
    list.length()
    list.search(4)
    list.insertAtBeg(10)
    list.display()
    print("Printing Insert after element ")
    list.insertaftergivenElement(1,20)
    list.insertaftergivenElement(10,40)
    list.insertaftergivenElement(5,34)
    list.display()
    print("++++++++++++++++++++++")
    list.insertAtGivenPosition(20,1)
    list.insertAtGivenPosition(30,3)
    list.display()
    list.delete(3)
    print("-----")
    list.display()






