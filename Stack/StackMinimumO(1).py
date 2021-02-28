class Node:
    def __init__(self,info):
        self.info = info
        self.next = None

class Stack :
    def __init__(self):
        self.top = None
        self.minimum = None

    def isEmpty(self):
        if self.top == None:
            print("Stack is Empty")
            return  True
        return False
    def getMinimum(self):
        if self.top == None:
            return "Stack is Empty"
        else:
            print("The minimum element in the stack is {0} ".format(self.minimum))

    def push(self,data):
        if self.top == None:
            self.top = Node(data)
            self.minimum = data # node.info
        elif data < self.minimum:
            temp = 2 * data - self.minimum
            newnode = Node(temp)
            newnode.next = self.top
            self.top = newnode
            self.minimum = data
        else:
            newnode = Node(data)
            newnode.next = self.top
            self.top = newnode

    def pop(self):
        if self.top == None:
            print("Stack Empty ")
            return

        topelement = self.top.info
        self.top = self.top.next

        if topelement < self.minimum:
            value = self.minimum
            self.minimum = 2 * self.minimum - topelement
            return value
        else :
             return topelement


    def peek(self):
        if self.isEmpty():
            print("Stack is empty ")
            return
        temp = self.top.info
        return temp

    def display(self):
        if self.top == None:
            print("Stack empty")
            return
        p = self.top
        print("Printing stack ")

        while p:
            print(p.info)
            p = p.next






if __name__=="__main__":
    stack = Stack()
    stack.isEmpty()
    print("Stack minimum " , stack.minimum)
    stack.push(5)
    stack.push(2)
    stack.push(7)
    stack.push(-1)
    stack.display()

    print("Stack minimum " , stack.minimum)


    print("popped " , stack.pop())



    print(stack.peek())

    stack.display()
