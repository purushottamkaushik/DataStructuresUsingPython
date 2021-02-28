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
            print(temp.info,sep=" ",end=" ")

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









if __name__=="__main__":
    list = LinkedListV2()
    list.insertAtEnd(1)
    list.insertAtEnd(2) # Insert at the end
    list.insertAtEnd(3)
    list.insertAtEnd(4)
    list.insertAtEnd(5)
    list.display()






