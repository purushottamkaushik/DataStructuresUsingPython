class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
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
    
    def count(self):
        count = 0
        temp = self.head
        
        while temp:
            count +=1
            temp = temp.next
        
        return count 

    def insertAtEnd(self,item):
        node = Node(item)
        if self.head is None:
            self.head = node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = node

        

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

    return third.head
    







if __name__ == "__main__":
    lst1 = LinkedList()
    lst2 = LinkedList()
    
 

  

    lst1.display()
    lst1.insertatbeg(4)
    lst1.insertatbeg(3)
    lst1.insertatbeg(2)
    lst1.insertatbeg(1)
    # lst1.display()
    count1 = lst1.count()

    lst2.insertatbeg(8)
    lst2.insertatbeg(7)
    lst2.insertatbeg(6)
    
    count2 = lst2.count()
    
    diff1 =0
    diff2 = 0
    if count1>count2:
        diff1 = count1 - count2
    else:
        diff2 = count2 - count1
    
    
    if diff1 !=0:
        for j in range(diff1):
            lst2.insertAtEnd(0)
    else:
        for j in range(diff2):
            lst1.insertAtEnd(0)
            
    print("Printing list 1")
    lst1.display()
    print("Printing list 2")
    lst2.display()
            
            
    
    
    
    
    lst3 = LinkedList()

    res = add(lst1.head, lst2.head, lst3)

    print("Printing res ")
    while res:
        print(res.data,end=" ")
        res = res.next
