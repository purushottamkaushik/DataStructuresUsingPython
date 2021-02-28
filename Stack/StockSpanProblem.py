
class Stack:
    def __init__(self):
        self.stack = [100, 80, 60, 70, 60, 75, 85]
        self.span = [1, 1, 1, 1, 1, 1,1 ]

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack) == 0 :
            print("Stack is empty")
            return

        item = self.stack.pop(-1)
        return item

    def peek(self):
        if len(self.stack ) == 0 :
            print("Stack is Empty ..")
            return
        return self.stack[-1]

    def stockspan(self):

        for i in range(1,len(self.stack)):
            count = 1
            for j in range(i-1,-1,-1):
                if self.stack[j] <= self.stack[i]:
                    count +=1
                else:
                    break


            self.span[i] = count
            pass
        pass

def calculateSpan(price, n, stock):
        s = Stack()
        s.push(0)  # Pushing the first element into the stack
        stock[0] = 1  # setting the stock for the first element to be 1 which is always

        for i in range(1, n):

            while s.isEmpty() == False  and price[s.peek()] <= price[i]:
                ele = s.pop()

            if s.isEmpty():
                stock[i] = i + 1
            else:
                stock[i] = i - s.peek()

            s.push(i)
        return stock

s = Stack()
print(s.stack)


s.stockspan()
print("After displaying ....")
print(s.stack)
print(s.span)
print("peek element " ,s.peek())
stack = [100, 80, 60, 70, 60, 75, 85]
stock = [1, 1, 1, 1, 1, 1,1]

print("Printing again ")
print(calculateSpan(stack,len(stack),stock))




