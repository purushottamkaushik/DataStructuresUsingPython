class Node:
    def __init__(self,data):
        self.info = data
        self.next = None
        return

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("List is empty")
        temp = self.head
        while temp:
            print(temp.info,sep="\t",end=" ")
            temp = temp.next
        print("")

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
        return count

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

    #
    # def KthNodeFromEnd(self,lst,k,length):
    #     x = length - k
    #     count = 0
    #     self.temp = self.head
    #
    #     while self.temp.next is not None:
    #         if count == x:
    #             return self.temp.info
    #         count+=1
    #         self.temp = self.temp.next


    # def KthNodeFromEnd(self,k,length):
    #     temp = self.head
    #     l = length - k
    #     for j in range(l):
    #         temp = temp.next
    #     return temp.info

    def KthNodeFromEnd(self,k,length):
        self.p = self.head
        self.q = self.head

        for j in range(k):
            self.q = self.q.next

        while self.q.next is not None:
            self.p =self.p.next
            self.q = self.q.next

        print("Returning element " , self.p.next.info)
        # print("Printitng q " , self.q.next)


if __name__=="__main__":
    lst = LinkedList()
    # n = int(input("ENter Number of elements "))
    # print("Enter n elements ")
    # for j in range(n):
    #     lst.insertAtEnd(int(input()))
    lst.insertAtEnd(1)
    lst.insertAtEnd(2)
    lst.insertAtEnd(3)
    lst.insertAtEnd(4)
    lst.insertAtEnd(5)
    print("Elements entered are ")
    lst.display()
    # k = int(input("Enter the K Value"))
    k = 2
    print("K value " , k)
    length = lst.length()
    lst.KthNodeFromEnd(k,length)



# LeetCode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def removeNthFromEnd(self, head: ListNode, n: int):
#
#         dummyNode = ListNode(0)
#         dummyNode.next = head
#
#         # first we will find the length of the list
#         length = 0
#         first = head
#
#         while first:
#             length += 1
#             first = first.next
#
#         first = dummyNode
#         length = length - n
#
#         while length > 0:
#             length -= 1
#             first = first.next
#
#         first.next = first.next.next
#
#         return dummyNode.next





# Only one pass implementation
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def removeNthFromEnd(self, head: ListNode, n: int):
#
#         dummyNode = ListNode(0)
#         dummyNode.next = head
#
#         first = dummyNode
#         second = dummyNode
#
#         for j in range(n + 1):
#             first = first.next
#
#         while first:
#             first = first.next
#             second = second.next
#
#         second.next = second.next.next
#
#         return dummyNode.next

