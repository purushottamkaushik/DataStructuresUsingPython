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
            return
        temp = self.head
        while temp.next is not self.head:
            print(temp.info)
            temp = temp.next
        print(temp.info)

    def insertAtEnd(self,data):
        self.data = Node(data)
        currNode = self.head  # head refers to the first node

        if self.head is None:
            self.head = self.data
        else:
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
        return count



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

    def detect_loop(self):
        slow = self.head
        fast = self.head

        while (slow and fast and fast.next ):
            slow = slow.next
            fast = fast.next.next

            if (slow == fast):
                print("Loop Found")
                return

        print("Loop not Found")


def splitCircular(head):
        slow = head
        fast = head
        temp1 = head
        temp2 = None


        while fast.next is not head and fast.next.next is not head:
            slow = slow.next
            fast = fast.next.next

        if fast.next.next is head:
            fast = fast.next
        if head.next != head:
            temp2 = slow.next

        fast.next = slow.next

        slow.next = head

        print("Successfully printed ")
        return temp1 , temp2





if __name__=="__main__":
    list = LinkedListV2()
    list.insertAtEnd(1)
    list.insertAtEnd(2)
    list.insertAtEnd(3)
    list.insertAtEnd(4)
    list.insertAtEnd(5)
    length = list.length()

    # list.head.next.next.next.next.next = list.head
    lst = list.head
    for j in range(1,length):
        lst = lst.next

    lst.next = list.head

    list1 = LinkedListV2()
    list2 = LinkedListV2()
    # list.detect_loop()
    list1.head ,list2.head =  splitCircular(list.head)

    print("Printing list1 Head ")
    print("List1 loop " , list1.detect_loop())
    list1.display()
    print("Printing list2 Head ")
    print("List2 loop " , list2.detect_loop())

    list2.display()







