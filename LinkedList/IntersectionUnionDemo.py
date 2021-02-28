class Node:
    def __init__(self,data):
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
            print(temp.data,end=" ")
            temp = temp.next
        print()

    def insertAtEnd(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = node

def intersection(head1 , head2):

    hashtable = dict()

    temp1 = head1
    temp2 = head2
    while temp1:

        item = temp1.data
        if item not in hashtable.keys():
            hashtable[item] = 1
        temp1 = temp1.next

    intersectionlist = LinkedList()

    while temp2:
        if temp2.data in list(hashtable.keys()):
            if intersectionlist.head is None:
                intersectionlist.head = Node(temp2.data)
            else:
                p = intersectionlist.head
                while p.next is not None:
                    p = p.next 
                p.next = Node(temp2.data)
        temp2 = temp2.next

    return intersectionlist.head

def count(head):
    if head is None :
        return 0
    temp = head
    count = 0
    while temp:
        count +=1
        temp = temp.next
    return count

def getUnion(head1 ,head2):
    count1 = count(head1)
    count2 = count(head2)

    small = None
    big  = None
    small1 = None
    if count1>count2:
        small = head2
        small1 = head2
        big = head1
    else:
        small = head1
        small1 = head1
        big = head2
    hashtable = set()
    while small:
        if small.data not in hashtable :
            hashtable.add(small.data)
        small = small.next

    print("Hashtable is  ", hashtable)


    unionlist = LinkedList()
    while big :

        if big.data not in hashtable:
            unionlist.insertAtEnd(big.data)
        else:
            unionlist.insertAtEnd(big.data)
            hashtable.remove(big.data)

        big = big.next


    print("hashtable again " , hashtable)

    while small1:
        print(small1.data)
        if small1.data in hashtable:
            unionlist.insertAtEnd(small1.data)
        small1 = small1.next

    print("Head is " , unionlist.head)
    return unionlist.head









if __name__=="__main__":
    lst1 = LinkedList()
    lst1.insertAtEnd(1)
    lst1.insertAtEnd(3)
    lst1.insertAtEnd(4)
    # lst1.insertAtEnd(4)
    lst1.insertAtEnd(5)

    lst1.display()

    lst2 = LinkedList()
    lst2.insertAtEnd(2)
    lst2.insertAtEnd(10)
    lst2.insertAtEnd(4)
    lst2.display()
    intersect = intersection(lst1.head,lst2.head)

    print("Printing intersection ")
    while intersect:
        print(intersect.data)
        intersect = intersect.next

    print("Printing Union ")
    union = getUnion(lst1.head , lst2.head)

    while union:
        print(union.data,end=" ")
        union = union.next



# class LinkedList:
#
#     def __init__(self):
#         self.head = None
#
#     def display(self):
#         temp = self.head
#         while (temp):
#             print("{} ->".format(temp.info)),
#             temp = temp.next
#         print("NULL")
#
#     def count(self):
#         count = 0
#         temp = self.head
#         while (temp):
#             count += 1
#             temp = temp.next
#         return count
#
#     def serach(self, value):
#         temp = self.head
#         pos = 1
#         while (temp):
#             if (temp.info == value):
#                 print("The value found at", pos)
#             temp = temp.next
#             pos += 1
#         print("Value not found in the linked list")
#
#     def insert_at_beg(self, data):
#         self.temp = node(data)
#         if self.head is None:
#             self.head = self.temp
#             return
#         self.temp.next = self.head
#         self.head = self.temp
#
#     def insert_at_end(self, data):
#         self.temp = node(data)
#         if self.head is None:
#             self.head = self.temp
#             return
#         self.p = self.head
#         while self.p.next is not None:
#             self.p = self.p.next
#         self.p.next = self.temp;
#
#     def insert_after_given_node(self, data, item):
#         self.p = self.head
#         while self.p is not None:
#             if (self.p.info == item):
#                 self.temp = node(data)
#                 self.temp.next = self.p.next
#                 self.p.next = self.temp
#                 return
#             self.p = self.p.next
#         print("Item not found")
#
#     def insert_at_pos(self, data, pos):
#         self.temp = node(data)
#         if pos == 1:
#             self.temp.next = self.head
#             self.head = self.temp
#             return
#         self.p = self.head
#         while pos > 2 and self.p is not None:
#             self.p = self.p.next
#             pos -= 1
#         if self.p is None:
#             print("Position exceeded the length of the list")
#         else:
#             self.temp.next = self.p.next
#             self.p.next = self.temp
#
#     def delete(self, data):
#         if self.head is None:
#             print("List is empty")
#             return
#         if self.head.info == data:
#             self.temp = self.head
#             self.head = self.head.next
#             return
#         self.p = None
#         self.curr = self.head
#         while self.curr is not None:
#             if self.curr.info == data:
#                 self.temp = self.p.next
#                 self.p.next = self.temp.next
#                 return
#             self.p = self.curr
#             self.curr = self.curr.next
#
#
# def divide(p):
#     q = p.next.next
#
#     while q is not None:
#         p = p.next
#         q = q.next
#         if q is not None:
#             q = q.next
#
#     start_second = p.next
#     p.next = None
#     return start_second
#
#
# def merge(head1, head2):
#     mergelist = None
#     if head1 == None:
#         return head1
#     if head2 == None:
#         return head2
#
#     if head1.info <= head2.info:
#         mergelist = head1
#         head1 = head1.next
#     else:
#         mergelist = head2
#         head2 = head2.next
#     temp = mergelist
#     while head1 and head2:
#         if head1.info <= head2.info:
#             temp.next = head1
#             temp = temp.next
#             head1 = head1.next
#         else:
#             temp.next = head2
#             temp = temp.next
#             head2 = head2.next
#
#     if head1 is None:
#         temp.next = head2
#     else:
#         temp.next = head1
#     return mergelist
#
#
# def mergeSort(head):
#     if head and head.next:
#         start_first = head
#         start_second = divide(head)
#         start_first = mergeSort(start_first)
#         start_second = mergeSort(start_second)
#         start_merged = merge(start_first, start_second)
#         return start_merged
#     else:
#         return head
#
#
# def getUnion(head1, head2):
#     union = LinkedList()
#     ele = 0
#     while (head1 is not None and head2 is not None):
#         if head1.info == head2.info:
#             ele = head1.info
#             head1 = head1.next
#             head2 = head2.next
#         else:
#             if head1.info < head2.info:
#                 ele = head1.info
#                 head1 = head1.next
#             else:
#                 ele = head2.info
#                 head2 = head2.next
#         union.insert_at_end(ele)
#     while head1 is not None:
#         union.insert_at_end(head1.info)
#         head1 = head1.next
#     while head2 is not None:
#         union.insert_at_end(head2.info)
#         head2 = head2.next
#     return union.head
#
#
# def getIntersection(head1, head2):
#     intersect = LinkedList()
#     while (head1 is not None and head2 is not None):
#         if head1.info == head2.info:
#             intersect.insert_at_end(head1.info)
#             head1 = head1.next
#             head2 = head2.next
#         else:
#             if head1.info < head2.info:
#                 head1 = head1.next
#             else:
#                 head2 = head2.next
#     return intersect.head
#
#
# if __name__ == '__main__':
#     llist1 = LinkedList()
#     llist2 = LinkedList()
#     list1 = LinkedList()
#     list2 = LinkedList()
#     print("Enter number of elements")
#     n = int(input())
#     print("Enter number of elements")
#     m = int(input())
#     print("enter elements")
#     for i in range(n):
#         llist1.insert_at_end(int(input()))
#     print("enter elements")
#     for i in range(m):
#         llist2.insert_at_end(int(input()))
#     llist1.head = mergeSort(llist1.head)
#     llist2.head = mergeSort(llist2.head)
#
#     list1.head = getUnion(llist1.head, llist2.head)
#     print("Union of list")
#     list1.display()
#     list2.head = getIntersection(llist1.head, llist2.head)
#     print("Intersection of lists")
#     list2.display()
