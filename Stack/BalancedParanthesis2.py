class Stack :

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0 

    def push(self,data):
        self.stack.append(data)


    def pop(self):
        if len(self.stack) == 0:
            print("Stack is Empty.. ")
            return
        item = self.stack.pop(-1)
        return item

    def display(self):
        if self.isEmpty():
            print("Stack is Empty ....") 
            return
        for j in range(len(self.stack)):
            print(self.stack[j])

    def peek(self):
        if self.isEmpty() :
            print("Stack is Empty ..")
            return
        print("Peak element is " , self.stack[-1])    

    def balanced(self,expression):

        for c in expression:
            if c=='(' or c == '{' or c == '[':
                self.stack.append(c)


            if len(self.stack ) == 0 :
                print("Not balanced ..")
                return


            if c == ')':
                x = self.stack.pop()
                if x != '(':
                    x = self.stack.pop()
                            













s = Stack()
# s.display()
# print("Stack is Empty " , s.isEmpty())

# s.push(1)
# s.push(2)
# s.push(3)

# s.display()
# s.pop()
# print("After popping ....")
# s.display()

# s.peek()
    