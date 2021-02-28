class Node:
    def __init__(self,data):
        self.info = data
        self.next = None


class CircularQ:
    def __init__(self):
        self.front = None
        self.rear = None

    def Enqueue(self,data):
        newNode = Node(data)
        if self.front is None:
            self.front = newNode
            self.rear = newNode
            self.rear.next = self.front
        else:
            self.rear.next = newNode
            self.rear = newNode
            self.rear.next = self.front




    def Dequeue(self):
        if self.front is None: # if the list is empty
            print("Queue is Empty ")
            return
        elif self.rear == self.front: # if there is only one item in the queue
            self.rear = self.front = None
            return
        else:
            self.rear.next = self.front.next
            self.front = self.front.next


    def isEmpty(self):
        return True if self.front == None else False

    def display(self):
        if not self.isEmpty():
            p = self.front
            while p.next != self.front:
                print(p.info)
                p = p.next
            print(p.info)
        else:
            print("Its an Empty Queue ")

if __name__=="__main__":
    q = CircularQ()
    print(q.isEmpty())
    q.display()
    q.Enqueue(1)
    q.Enqueue(2)
    q.Enqueue(3)
    q.display()
    q.Dequeue()
    q.Dequeue()
    q.Dequeue()
    print("After Dequeue Operation.. ")
    q.display()