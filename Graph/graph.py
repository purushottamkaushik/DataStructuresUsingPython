class Graph:

	def __init__(self,size):
		self.adMatrix = [] * size

		for i in range(size):
			self.adMatrix.append([0 for i in range(size)])

	def add_edge(self ,v1 ,v2):
		if v1 == v2 :
			print("V1 and V2 are same...")
			return
		if self.adMatrix[v1][v2] == 0:
			self.adMatrix[v1][v2] = 1
			self.adMatrix[v2][v1] = 1

	def remove_edge(self,v1,v2):
		if v1 == v2 :
			print("V1 and V2 are same ")
			return
		if self.adMatrix[v1][v2] == 1:
			self.adMatrix[v1][v2] = 0
			self.adMatrix[v2][v1] = 0

	def printMatrix(self):
		for i in range(len(self.adMatrix)):
			print(self.adMatrix[i])

			



g = Graph(4)		
print(g.adMatrix)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,2)
g.add_edge(2,3)

g.printMatrix()
g.remove_edge(0,1)
print("After removing Edge ")
g.printMatrix()