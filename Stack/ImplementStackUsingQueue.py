class Stack:
	def __init__(self):
		self.queue = []

	def push(self,item):
		self.queue.append(item)

	def pop(self):
		if len(self.queue) == 0 :
			return "Cannot pop From  Empty Stack"
		else:
			item =self.queue.pop(-1)
			return item

	def checkIsEmpty(self):
		return len(self.queue) == 0		
			
	def printStack(self):
		if self.checkIsEmpty():
			print("Stack is Empty");
			return
		else:
			for i in range(-1,-len(self.queue)-1 , -1):
				print(self.queue[i])

stack = Stack()
print("Checking Stack Empty or not :" ,stack.checkIsEmpty())
print(stack.pop())
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.queue)
print("Checking Stack Empty or not :" ,stack.checkIsEmpty())
print("Printing Stack : ")
stack.push(4)
print("Printing stack Again")
print(stack.queue)

print("------------------------------------------------------------------")
print(stack.pop())
print(stack.queue)
