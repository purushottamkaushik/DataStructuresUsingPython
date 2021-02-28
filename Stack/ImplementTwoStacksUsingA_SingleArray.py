class Stack :
    def __init__(self):
        self.maxsize = 5

        self.top1 = -1
        self.top2 = self.maxsize
        self.stack = [0] * self.maxsize


    def push1(self,element):
        if self.top1  < self.top2-1:
            self.top1 +=1
            # print("Top1 {} and element {}".format(self.top1,element))
            self.stack[self.top1] = element
            print("Element Inserted Current Stack: " , self.stack)

        else:
            print("Stack OverFlow ")
            return

    def pop1(self):
        if self.top1 <0:
            print("Stack UnderFlow")
            return
        else:
            item = self.stack[self.top1]
            self.stack[self.top1] = 0
            self.top1 -=1
            print("Top1 is {} and item removed is {}".format(self.top1,item))
            print("Current Stack is Elements are " , self.stack)
            return item


    def push2(self,element):
        if self.top1 < self.top2-1:
            self.top2 -= 1
            self.stack[self.top2] = element
            print("Element {} pushed into the stack ".format(element))

            print("Stack Now contains ", self.stack)

        else:
            print("Stack overflow")
            return


    def pop2(self):
        if self.top2 > self.maxsize - 1:
            print("UnderFlow stack 2")
            return
        else:
            item = self.stack[self.top2]
            self.stack[self.top2] = 0
            self.top2 +=1
            print("Item popped from the stack is ",item)
            print("Stack now contains " , self.stack)




s = Stack()
s.push1(10)
s.push1(5)
s.push1(3)

s.pop1()
s.push2(20)
s.push2(30)
s.push2(40)
s.push2(50)
s.push2(100)
# s.pop1()
# s.pop1()
# s.pop1()

s.pop2()
s.pop2()
s.pop2()
s.pop2()
