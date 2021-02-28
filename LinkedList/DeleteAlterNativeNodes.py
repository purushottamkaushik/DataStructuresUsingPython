# https://www.hackerrank.com/contests/applied-course/challenges/delete-nodes-in-a-linked-list


# Write a program to delete n Nodes in the linked list after skipping m Nodes in the linked list.

# Input Format

# First line contains the N size of input elements followed by n and m.
# Second line contains N integer values
# Constraints

# 1 < N < 10^6

# Output Format

# In output print the list after deleting the nodes.

# Sample Input 0



class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("List empty")
            return

        temp = self.head
        while temp:
            print(temp.data ,sep=" ",end=" ")
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

    def deleteAlternativeNode(self):
        lst = []
        self.p = self.head
        currnode = self.head.next
        while currnode:
            self.temp = currnode
            self.p.next = self.temp.next
            currnode = self.temp.next
            self.p = self.temp





        # print(self.p.data)
        # print(self.temp.data)
        # lst.append(self.temp.data)
        # self.temp = self.temp.next
        # print(self.temp)
        #
        # # self.head = self.temp
        # return  lst #self.temp



if __name__=="__main__":
    lst = LinkedList()
    lst.display()  
    lst.insertAtEnd(1)
    lst.insertAtEnd(2)  
    lst.insertAtEnd(3)
    lst.insertAtEnd(4)
    lst.insertAtEnd(5)
    lst.insertAtEnd(6)
    # lst.insertAtEnd(7)
    lst.display()    
    
    print("Printing remaining list " , lst.deleteAlternativeNode())
    print("List display")
    lst.display()                       