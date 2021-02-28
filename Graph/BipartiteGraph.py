class Bipartite:
	def __init__(self,size):
		self.V = size
		self.starttime = [0] * size
		self.endtime = [0] * size
		self.graph = {0:[1],1:[2,4],2:[1,3],3:[],4:[1],5:[6],6:[]}
		self.pred = [-1] * size
		self.colors = ['white'] * size
		self.bcolor = [0] * size

	def checkcolor(self , u ,v) :
		print(u , v)
		if self.bcolor[u] == self.bcolor[v]:
			print("Not bipartite")
			return


	def assigncolor(self , u , v) :
		if self.bcolor[u] == 0:
			self.bcolor[v] = 1
		else:
			self.bcolor[v] = 0 	




	def dfsvisit(self,i):
		self.time +=1
		self.starttime = self.time
		self.colors[i] = 'gray'

		for v in self.graph[i]:
			if self.colors[v] == 'white':
				self.pred[v] = i
				self.assigncolor(i,v)
				self.dfsvisit(v)
			else:
				self.checkcolor(i,v)		

		self.time +=1
		self.endtime[i] = self.time
		self.colors[i] = 'black'


		
	def bipartite(self):
		for u in range(self.V):
			self.time = 0
			if self.colors[u] == 'white':
				self.bcolor[u] = 0
				self.dfsvisit(u)


b = Bipartite(7)
b.bipartite()
print(b.bcolor)

