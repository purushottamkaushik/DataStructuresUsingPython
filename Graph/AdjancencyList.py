class Node:
	def __init__(self,v):
		self.vertex = v
		self.next = None


class Graph:

	def __init__(self,size):
		self.size = size
		self.graph = [None] * size

	def add_edge(self,s,d):
		if s == d :
			print("Source and Destination are same ...")
			return
		# Creating a Link from Destination to source 	
		node = Node(d)	
		node.next = self.graph[s]
		self.graph[s] = node

		# Creating a Link From Source to Destination

		node = Node(s)
		node.next = self.graph[d]
		self.graph[d] = node


	def printMatrix(self):
		for i in range(self.size):
			temp = self.graph[i]
			while temp:
				print(temp.vertex)
				temp = temp.next
			print("Loop Fininshed ...")	





g = Graph(4)		
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,2)
g.add_edge(2,3)

g.printMatrix()
# g.remove_edge(0,1)
print("After removing Edge ")
g.printMatrix()