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

    def delete(self,m,n):
        
        currnode = self.head
        self.prev = None

        for i in range(m):
            self.prev = currnode
            currnode = currnode.next
        print("Current Node " , currnode.data)
        print("Previous Node " , self.prev.data)

        for j in range(n):
            self.prev.next = currnode.next
            currnode = currnode.next

        print("Current Node ", currnode.data)
        print("Previous Node ", self.prev.data)


if __name__=="__main__":
    lst = LinkedList()
    lst.display()  
    lst.insertAtEnd(1)
    lst.insertAtEnd(2)  
    lst.insertAtEnd(3)
    lst.insertAtEnd(4)
    lst.insertAtEnd(5)
    lst.insertAtEnd(6)
    lst.insertAtEnd(7)
    lst.display()   
    lst.delete(4,2)
    print("List display ")
    lst.display()                   