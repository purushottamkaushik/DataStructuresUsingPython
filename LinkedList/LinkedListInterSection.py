
class Node:
    def __init__(self,data):
        self.info = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("EMpty list")
            return
        temp = self.head

        while temp:
            print(temp.info,end=" ")
            temp =temp.next
        print()

    def insertAtEnd(self,data):
        temp = Node(data)
        if self.head is None:
            self.head = temp
            return

        p = self.head
        while p.next is not None :
            p = p.next

        p.next = temp

    def count(self):
        count = 0 
        temp = self.head
        while temp:
            count +=1
            temp = temp.next    
        
        return count


def intersection(lst1,lst2):
    count1 = 0

    temp1 = lst1.head
    temp2 = lst2.head

    while temp1:
        count1 +=1
        temp1 = temp1.next
    count2 = 0
    while temp2:
        count2 +=1
        temp2 = temp2.next
    print("List 1 count " , count1)

    count2 = lst2.count()
    print("List 2 count " , count2)

    first = lst1.head
    second = lst2.head

    if (count1>count2):
        diff = count1 - count2
    else:
        diff = count2 - count1

    for j in range(diff):
        first =first.next

    while first is not None and second is not None:
        if first.info == second.info:
            print("Intersection at " , first.info )
            return
        first = first.next
        second = second.next

    print("First " , first)
    print("Second " ,second)    
    print("No intersection found")




if __name__=="__main__":
    lst1 = LinkedList()
    lst1.display()
    lst1.insertAtEnd(1)
    lst1.insertAtEnd(2)
    lst1.insertAtEnd(3)
    lst1.insertAtEnd(4)
    lst1.insertAtEnd(5)
    lst1.display()
    
    lst2 = LinkedList()
    lst2.insertAtEnd(1)
    lst2.insertAtEnd(1.5)
    

    lst2.display()
    intersection(lst1,lst2)

    t1  = lst2.head
    while t1.next is not None:
        print(t1.info ,end=" ")

        t1 = t1.next
       
    t1.next = lst1.head.next.next.next

    lst1.display()
    lst2.display()

    intersection(lst1,lst2)


    # print("Finding Intersection of list2 and list 3")
    # intersection(lst2.head,lst3.head)


