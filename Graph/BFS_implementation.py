class BFS:

	def __init__(self,size):
		self.distance = [0] * size
		self.colors = ['white'] * size
		self.pred = [-1] * size
		self.graph = {0:[1], 1:[0, 2], 2: [1, 3], 3: [2, 4, 5],
		4: [3, 5, 7], 5: [3, 4, 6, 7], 6: [5, 7], 7:[4, 5, 6]}

	def bfs(self,source):
		
		q = [] # Implementation of queqe as a list
		q.append(source) # Insert First vertex into Queue
		self.distance[source] = 0 # Initialize Distance of the source vertex to be 0
		self.colors[source] = 'gray' # Initialize the color of the source vertex to be gray 
		self.pred[source] = None # Setting the predecessor to be None 

		while q: # while the queue is not Empty
			current = q.pop(0) # Removing the first element from the queue
			print(current) # Printing the current element
			for i in range(len(self.graph[current])): # Finding Adjacent Vertex 
				if self.colors[self.graph[current][i]] == 'white': # if Adjacent vertex color is white 
					self.colors[self.graph[current][i]] = 'gray' # change color 
					self.distance[self.graph[current][i]] = self.distance[current] + 1 # update distance
					self.pred[self.graph[current][i]] = current # update predecessor 
					q.append(self.graph[current][i]) # Append the current vertex to the queue
				#q.append(self.graph[current][i])
			
			self.colors[current]  = 'black' # change the current vertex color to black 


				
b = BFS(8)
b.bfs(2)


