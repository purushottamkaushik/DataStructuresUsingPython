class Heap :

	def heapify(self,arr,n,i):
		"""
			It is a helper method to perform heapify operation in the process
			In this case min heapify and returns the result after operation
			Also it uses recursion extensively and time complexity is not trivial 
			
		"""
		smallest = i
		left = 2*i + 1
		right = 2*i + 2

		if left < n and arr[left] < arr[smallest]:
			smallest = left

		if right < n and arr[right] < arr[smallest]:
			smallest = right

		if smallest != i :
			arr[smallest] ,  arr[i] = arr[i] , arr[smallest]
			self.heapify(arr,n,smallest)		


	def buildminheap(self,arr,n):
		"""
		It is a method that is used to build a minheap using array representation of the 
		Heap data structure
		"""

		for j in range(n//2,-1,-1):
			self.heapify(arr,n,j)
		



arr = [4 ,1,3,2,16,9,10,14,8,7]
n = len(arr)
print("Printing array : " , arr)
minheap = Heap()
minheap.buildminheap(arr,n)
print("MinHeap is :" , arr)
