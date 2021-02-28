class Heap:

    def heapify(self,arr,n,i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[i] < arr[left]:
            largest = left

        if right < n and arr[largest] < arr[right]:
            largest = right

        if largest != i :
            arr[largest] , arr[i] = arr[i] , arr[largest]
            self.heapify(arr,n,largest)



    def buildmaxheap(self,arr,n):
        l = len(arr)

        for i in range(l//2,-1,-1):
            self.heapify(arr,l,i)

    def heapsort(self,arr):
        l = len(arr)
        self.buildmaxheap(arr,l)
        for i in range(l-1,0,-1):
            arr[i] , arr[0] = arr[0] , arr[i]
            self.heapify(arr,i,0)


arr  = [4,1,3,2,16,9,10,14,8,7]
print(arr)
h = Heap()
h.buildmaxheap(arr,len(arr))
print(arr)
print("sorted")

h.heapsort(arr)
print(arr)

