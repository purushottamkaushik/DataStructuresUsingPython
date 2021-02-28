class Node:
    def __init__(self,data):
        self.info = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def display(self):

        temp = self.head # Pointing to the first node
        # print(temp)
        if temp:
            while (temp): # while it reaches to the null value
                  print(temp.info) # Node info print
                  temp = temp.next # Storing the next pointer
        else:
            print("LinkedList is empty ")

    def insertAtEnd(self, item):
        node  = Node(item)
        if self.head is None:
            self.head = node
        else:
            temp = self.head # Points to a node
            # print("Printing self.head " , self.head)
            while temp.next != None:
                temp = temp.next

            temp.next = node

    def length(self):
        total = 0
        temp = self.head
        while temp != None : # if the list does reach its end
            total+=1
            temp = temp.next
        print("Printing length " , total)


    def search(self,item):
        pos = 0
        temp = self.head

        while temp:
            pos +=1
            if temp.info == item:
                print("Found at position ",pos)
                return
            temp = temp.next
        print("Element Not Found in the list ")


    def insertAtBeg(self,item):
        """
        head contains address,
        Node contains data and address of the next node
        """
        self.temp = Node(item) # Creating a temporary Node with the data
        if self.head is None : # if head of list is null then the temp node is our first node so head should be pointing
            # to that node
            self.head = self.temp

        self.temp.next = self.head # temporary node next field head address
        self.head = self.temp # head pointing to the temporary node

    def insertaftergivenElement(self,item,data):
        currNode = self.head

        while currNode.next is not None:
            if currNode.info == item:
                self.temp = Node(data)
                self.temp.next = currNode.next
                currNode.next = self.temp
                return
            currNode = currNode.next

        print("Item " , item ," Not found in the list ")


    def insertAtGivenPosition(self,data,pos):
        self.newNode = Node(data)
        if pos == 1:
            self.newNode.next = self.head
            self.head = self.newNode
            return
        self.temp = self.head

        while pos > 2 and self.temp is not None:
            self.temp = self.temp.next
            pos-=1
        # print(self.temp)
        if self.temp is None:
            print("Position doesnt Exist in the List")
        else:
            self.newNode.next = self.temp.next
            self.temp.next = self.newNode

    def delete(self,data):
        # case 1 if the list is empty
        if self.head is None:
            print("Empty list")
            return
        # case 2 if we have to remove the first element
        if self.head.info == data:
            self.temp = self.head
            self.head = self.head.next
            return

        # case 3 if we have to remove the element in position greater than the first position
        self.p = None
        self.curr = self.head

        while self.curr is not None:

            if self.curr.info == data:
                self.temp = self.p.next
                self.p.next = self.temp.next
                return
            self.p = self.curr
            self.curr = self.curr.next





if __name__=="__main__":
    list = LinkedList()
    list.display()
    list.insertAtEnd(2) # Insert at the end
    list.insertAtEnd(3)
    list.insertAtEnd(4)
    list.display()
    print("--------------------")
    # list.length()
    # list.search(4)
    # list.insertAtBeg(10)
    # list.insertAtBeg(12)
    # list.display()
    # print("------------------------------------------------")
    list.insertaftergivenElement(2,20)
    list.insertaftergivenElement(3,40)
    list.insertaftergivenElement(5,34)
    list.display()
    print("++++++++++++++++++++++")
    list.insertAtGivenPosition(20,1)
    list.insertAtGivenPosition(30,3)
    list.display()
    list.delete(3)
    print("-----")
    list.display()






