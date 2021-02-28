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
            print(temp.info,sep=" ",end="\n")
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

def reverse(head):
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
        else:
            return False
    if lst1 is None and lst2 is None:
        return True
    else:
        return False

def palindrome(llst):
        head = llst.head
        slowptr = head
        fastptr = head
        slow_prev = None
        midnode = None

        if (head is not None and head.next is not None):
            while fastptr is not None and fastptr.next is not None:  # for iteration of the whole list
                slow_prev = slowptr
                slowptr = slowptr.next
                fastptr = fastptr.next.next



            if fastptr is not None:  # for odd number of nodes
                midnode = slowptr
                slowptr = slowptr.next

            nexthalf = slowptr
            slow_prev.next = None
            nexthalf = reverse(nexthalf)
            res = compare(head, nexthalf)
            nexthalf = reverse(nexthalf)
            # a = 10
            if midnode is not None: # odd number of nodes
                slow_prev.next = midnode
                midnode.next = nexthalf
            else:
                slow_prev.next = nexthalf

        # print(a)
        return res





if __name__=="__main__":
    lst = LinkedList()
    # lst.display()

    lst.insertAtEnd(1)
    lst.insertAtEnd(2)
    # lst.insertAtEnd(3)
    # lst.insertAtEnd(4)
    # lst.insertAtEnd(3)
    lst.insertAtEnd(2)
    lst.insertAtEnd(1)
    # lst.insertAtEnd(2)
    # lst.insertAtEnd(0)


    lst.display()
    # lst.detect_loop()
    # print("After reversing ")
    # lst.reverse()
    # lst.display()

    # print("Palindrome or not" )
    # palindrome(lst)
    if True is    palindrome(lst):
        print("Palindromic LinkedList")
    else:
        print("Not a palindromic LinkedList ")
    lst.display()

    # lst.head.next.next = lst.head.next
    # lst.detect_loop()