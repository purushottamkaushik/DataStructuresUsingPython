class Stack:
    def __init__(self):
        self.stack = []
        # return  self.stack

    def push(self,item):
        self.stack.append(item)

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def display(self):
        if stack.isEmpty():
            print("Empty stack ")
            return

        for i in range(len(self.stack)):
            print(self.stack[i],sep=" " ,end=" ")

    def pop(self):
        if len(self.stack) == 0:
            print("Empty stack ")
            return

        return self.stack.pop()

if __name__=="__main__":
    stack = Stack()
    # if True is stack.isEmpty():
    #     print("Empty stack")
    # else:
    #     print("Not an Empty stack")
    #
    stack.display()
    stack.push(1)
    stack.push(3)
    stack.push(2)
    stack.display()


    print("\nStack item removedd " , stack.pop())
    stack.display()


