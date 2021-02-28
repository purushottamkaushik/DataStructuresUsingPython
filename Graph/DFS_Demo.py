from collections import defaultdict
class DFS:

	def __init__(self,size):
		self.V  =size
		self.starttime = [0] * size
		self.endtime = [0] * size
		# self.pred = [-1] * size
		self.colors = ['white'] * size
		self.graph = defaultdict(list)


	def add_edge(self , u , v):
		self.graph[u].append(v)


	def dfsvisit(self,i):
		self.time += 1
		self.starttime[i] = self.time
		self.colors[i] = 'gray'

		for j in self.graph[i]:
			if self.colors[j] == 'white':
				# self.pred[j] = i 
				self.dfsvisit(j)
		
		self.time +=1
		self.endtime[i] = self.time
		self.colors[i] = 'black'




	def dfs(self):
		for i in range(self.V):
			self.time = 0
			if self.colors[i] =='white':

				self.dfsvisit(i)



d = DFS(6)
d.add_edge(0, 1)
d.add_edge(0, 2)
d.add_edge(1, 2)
d.add_edge(2, 3)
d.add_edge(3, 1)
d.add_edge(4, 3)
d.add_edge(4, 5)
d.add_edge(5, 5)
d.dfs()

print(d.starttime)
print(d.endtime)