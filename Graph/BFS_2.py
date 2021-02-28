
class BFS:
	def __init__(self,size):
		self.distance = [0] * size
		self.pred = [-1] * size
		self.colors = ['white'] * size
		self.graph = {0:[1], 1:[0, 2], 2: [1, 3], 
		3: [2, 4, 5], 4: [3, 5, 7], 5: [3, 4, 6, 7], 6: [5, 7], 7:[4, 5, 6]}

	def bfs(self , source ):
		q = []
		q.append(source)
		self.pred[source] = None
		self.distance[source] = 0
		self.colors[source] = 'gray'

		while q:
			current = q.pop(0)
			print(current)
			for i in range(len(self.graph[current])):
				if self.colors[self.graph[current][i]] == 'white':
					self.colors[self.graph[current][i] ] = 'gray'
					self.distance[self.graph[current][i]] = self.distance[current] + 1
					self.pred[self.graph[current][i] ] = current

					q.append(self.graph[current][i])

			self.colors[current] = 'black'


bfs = BFS(8)
bfs.bfs(2)					
			