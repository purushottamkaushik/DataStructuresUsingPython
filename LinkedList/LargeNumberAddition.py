class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("Empty list")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def insertatbeg(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        node.next = self.head
        self.head = node


# def add(first, second, third):
#     prev = None
#     temp = None
#     carry = 0
#
#     while first is not None or second is not None:
#         fdata = 0 if first.data is None else first.data
#         sdata = 0 if second.data is None else second.data
#
#         sum = fdata + sdata + carry
#
#         carry = 1 if sum >= 10 else 0
#
#         sum = sum if sum <10 else sum%10
#         temp = Node(sum)
#         print(temp.data)
#         if third.head is None:
#             third.head = temp
#         else:
#             prev.next = temp
#         prev = temp
#
#         if first is not None:
#             first = first.next
#         # print("First is " , first.data)
#         if second is not None:
#             second = second.next
#
#     #
#     if carry > 0:
#         temp.next = Node(carry)
#
#     print("The sum is :")
#     t1 = third.head
#
#     while t1:
#         print(t1.data, end=" ")
#         t1 = t1.next
#



def add(first ,second, third):
    prev =None
    temp = None
    carry = 0

    while first is not None or second is not None:

        fdata = 0 if first.data is None else first.data
        sdata = 0 if second.data is None else second.data

        sum = fdata + sdata + carry

        carry = 1 if sum>=10 else 0
        sum = sum if sum<10 else sum%10

        temp = Node(sum)

        if third.head is None:
            third.head = temp
        else:
            prev.next = temp

        prev = temp

        if first is not None:
            first = first.next
        if second is not None:
            second = second.next

        if carry > 0:
            temp.next = Node(carry)

    t1 = third.head
    print("Printing List")
    while t1:
            print(t1.data,end=" ")
            t1 = t1.next


























if __name__ == "__main__":
    lst1 = LinkedList()
    lst1.display()
    lst1.insertatbeg(4)
    lst1.insertatbeg(3)
    lst1.insertatbeg(2)
    lst1.insertatbeg(1)
    lst1.display()

    lst2 = LinkedList()
    lst2.insertatbeg(8)
    lst2.insertatbeg(7)
    lst2.insertatbeg(6)
    lst2.insertatbeg(5)
    lst2.display()
    lst3 = LinkedList()

    add(lst1.head, lst2.head, lst3)
