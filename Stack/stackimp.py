class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            return -1

    def peek(self):
        # return self.stack[len(self.stack)-1]
        return self.stack[-1]

if __name__=="__main__":
    stack = Stack()
    print(stack.isEmpty())
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.isEmpty())
    print(stack.stack) # printing the instance variable using the object
    stack.pop()
    print(stack.stack)
    print("Peek Element is " , stack.peek())



