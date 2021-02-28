class Node:
    def __init__(self,data):
        self.info = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("Empty list ")
            return

        temp = self.head
        while temp:
            print(temp.info,sep=" ",end=" ")
            temp = temp.next

    def insertAtEnd(self,data):
        self.temp = Node(data)

        if self.head is None:
            self.head = self.temp
            return

        self.p = self.head
        while self.p.next is not None:
            self.p = self.p.next

        # print(self.p)
        self.p.next = self.temp


    # def detect_loop(self):
    #     slow = self.head
    #     fast = self.head
    #
    #     while (slow and fast and fast.next ):
    #         slow = slow.next
    #         fast = fast.next.next
    #
    #         if (slow == fast):
    #             print("Loop Found")
    #             return
    #
    #     print("Loop not Found")


    def detect_loop(self):
        """This is the method uses hashing techniques """
        myhastable = dict()

        temp = self.head

        while temp:
            address = id(temp)
            if address not in myhastable.keys():
                myhastable[address] = 1
            else:
                print("Loop Found")
                return 1
            temp = temp.next

        print("Loop Not Found")
        return 0

    def palindrome(self):
        llst = self.head
        slowptr = self.head
        fastptr = self.head
        slow_prev = None
        midnode = None
        nextHalf = None

        if (self.head is not None and self.head.next is not None):
            while fastptr is not None and fastptr.next is not None:  # for iteration of the whole list
                slow_prev = slowptr
                slowptr = slowptr.next
                fastptr = fastptr.next.next

            if fastptr.next is None:  # for odd number of nodes
                midnode = slowptr
                nextHalf = slowptr.next

            nextHalf = slowptr
            slow_prev.next = None
            nextHalf = self.reverse(nextHalf)
            res = compare(self.head, nextHalf)
            nextHalf = self.reverse(nextHalf)

            if midnode is None:
                slow_prev.next = midnode
                midnode.next = nextHalf
            else:
                slow_prev.next = nextHalf
        else:
            print("Palindrome")

    def reverse(self,head):
        prev = None
        current = head

        while current:
            Next = current.next
            current.next = prev
            prev = current
            current = Next

        head = prev
        return head


def compare(lst1,lst2):
    while lst1 is not None and lst2 is not None:
        if lst1.info == lst2.info:
            lst1 = lst1.next
            lst2 = lst2.next

    if lst1 is None and lst2 is None:
        return True
    else:
        return False










        # else:
        #     print("Palindrome")



if __name__=="__main__":
    lst = LinkedList()
    # lst.display()

    lst.insertAtEnd(1)
    lst.insertAtEnd(2)
    lst.insertAtEnd(3)
    lst.insertAtEnd(4)
    lst.insertAtEnd(3)
    lst.insertAtEnd(2)
    lst.insertAtEnd(1)


    lst.display()
    # lst.detect_loop()
    # print("After reversing ")
    # lst.reverse()
    # lst.display()

    # print("Palindrome or not" )
    lst.palindrome()
    print()
    lst.display()

    # lst.head.next.next = lst.head.next
    # lst.detect_loop()