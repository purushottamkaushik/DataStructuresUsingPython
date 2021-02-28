class Heap :
	
	def heapify(self,arr, n ,i ):
		# Here arr is the array representation of the heap 
		# n is the size of the array 
		# i is the index of the root node
		largest = i
		left = 2 * i + 1
		right = 2 * i + 2

		# Finding the index of largest element from left node and root node
		if left < n and arr[left] > arr[largest]:
			largest = left
		# Finding the index of the largest element from root node and right node	
		if right < n and arr[right] > arr[largest]:
			largest = right

		# Swapping root node with one of the nodes if root is not the largest 
		if largest != i:
			arr[i] , arr[largest] = arr[largest] , arr[i]
			self.heapify(arr,n , largest)		 



	def buildMaxHeap(self,arr,n):
		for j in range(n//2 , -1,-1):
			self.heapify(arr,n,j)

			
arr = [4 ,1,3,2,16,9,10,14,8,7]
print(arr)	
heap = Heap()
heap.buildMaxHeap(arr,len(arr))
print(arr)


