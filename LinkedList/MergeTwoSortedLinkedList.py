class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedListV2:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("List is empty")
        temp = self.head
        while temp:
            print(temp.data,sep=" ",end=" ")

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

    def length(self):
        count = 0
        temp = self.head
        while temp:
            count +=1
            temp = temp.next
        print("Length of the list is " , count)
        return None

def merge(head1,head2):
    temp = None
    mergelist = None
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    if head1.data <= head2.data:
        mergelist = head1
        head1 = head1.next
    else:
        mergelist = head2
        head2 = head2.next

    temp = mergelist

    while head2 is not None and head1 is not None:
        if head1.data <= head2.data:
            temp.next = head1
            temp = temp.next
            head1 = head1.next
        else:
            temp.next = head2
            temp = temp.next
            head2 = head2.next


    if head2 is None:
        temp.next = head1
    else:
        temp.next = head2

    return mergelist






if __name__=="__main__":
    list1 = LinkedListV2()
    list1.insertAtEnd(2)
    list1.insertAtEnd(4) # Insert at the end
    list1.insertAtEnd(6)
    list1.insertAtEnd(8)
    list1.display()

    list2 = LinkedListV2()
    list2.insertAtEnd(1)
    list2.insertAtEnd(3)
    list2.insertAtEnd(5)
    list2.insertAtEnd(9)
    list2.display()

    mergelist = merge(list1.head,list2.head)

    while mergelist:
        print(mergelist.data ,sep=" ",end=" ")
        mergelist = mergelist.next





