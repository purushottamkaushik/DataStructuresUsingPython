class Node:
    def __init__(self, info):
        self.info = info
        self.next = None


class Queue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, data):
        newnode = Node(data)
        if self.rear is None:
            # Queue is empty so both front and rear must point to the same first node

            self.front = newnode
            self.rear = newnode
        else:
            self.rear.next = newnode
            self.rear = newnode

    def isEmpty(self):
        if self.rear is None and self.front is None:
            return True
        # else:
        #     print("Queue is Empty....")
        #

    def dequeue(self):
        # checking the base case
        if self.isEmpty():
            print("There is no element in the queue ")
            return
        temp = self.front
        self.front = temp.next
        temp = None

    def display(self):
        if not self.isEmpty():
            p = self.front
            while p:
                print(p.info, end=" ")
                p = p.next
        if self.front == None:
            print("Queue is Empty.")


if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.display()
    print("\n******")
    q.dequeue()
    q.display()
    print("\n***********")
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.display()
