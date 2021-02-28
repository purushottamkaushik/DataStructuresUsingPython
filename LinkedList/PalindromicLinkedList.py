class Node:
    def __init__(self,data):
        self.info = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("Empty  List")
            return

        temp = self.head
        while temp:
            print(temp.info ,end=" ")
            temp = temp.next
        print()     
    def insertAtEnd (self,item):
        tempNode = Node(item)
        if self.head is None:
            self.head = tempNode
            return
        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = tempNode


def reverse(head):
        prev = None
        currNode = head

        while currNode:
            Next = currNode.next
            currNode.next = prev
            prev = currNode
            currNode = Next

        head = prev
        return head 

def compare(head1 , head2):
    while head1 is not None and head2 is not None:
        if head1.info == head2.info:
            head1 = head1.next
            head2 = head2.next
        else:
            return False
    return True             

def ispalindromic(lst):
    head = lst.head
    slowptr = head
    fastptr = head
    midnode = None
    nexthalf = None
    slowprev = None 
    if head is not None and head.next is not None:
        while fastptr and fastptr.next :
            slowprev = slowptr
            slowptr = slowptr.next
            fastptr = fastptr.next.next

        if fastptr is not None:
            midnode = slowptr
            slowptr = slowptr.next

        nexthalf = slowptr
        slowprev.next = None
        nexthalf = reverse(nexthalf)
        res = compare(head,nexthalf)
        nexthalf = reverse(nexthalf)

        if midnode is not None:
            slowprev.next = midnode
            midnode.next = nexthalf    
        else:
            slowprev.next = nexthalf        

        return res

if __name__ == "__main__":
    lst = LinkedList()
    lst.insertAtEnd(1)    
    lst.insertAtEnd(2)
    # lst.insertAtEnd(3)
    lst.insertAtEnd(2)
    lst.insertAtEnd(1)
    lst.display()
    print("After reverse ")
    
    if True is ispalindromic(lst):
        print("Palindromic List") 
    else:
        print("Not a Palindromic list")       

    lst.display()