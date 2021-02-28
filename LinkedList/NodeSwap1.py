class Node:

    def __init__(self,data):
        self.info = data
        self.next = None


class LinkedList:

    def __init__(self):
        print("L1 created")
        self.head = None

    def display(self):
        if self.head is None:
            print("Empty list ")
            return
        temp = self.head
        while temp:
            print(temp.info,sep="\t",end=" ")
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


    def swap(self,k):

        dummyNode = Node(0)
        dummyNode.next = self.head
        first = dummyNode
        second = dummyNode
        for j in range(k+1):
            first = first.next

        while first:
            first = first.next
            second = second.next

        self.temp = second.next
        print("Temp.info " , self.temp.info)
        second.next = second.next.next
        # print("Printing first " , first)
        # print("Second info " , second.info)
        # k -=1
        # tempnode = dummyNode
        # print("K is " , k)
        # for j in range(k):
        #     tempnode = tempnode.next
        #
        # tempnode.next = self.temp
        # self.temp.next = tempnode.next
        #








if __name__=="__main__":
    lst = LinkedList()
    lst.insertAtEnd(10)
    lst.insertAtEnd(3)
    lst.insertAtEnd(1)
    lst.insertAtEnd(9)
    lst.display()
    lst.swap(3)
    lst.display()