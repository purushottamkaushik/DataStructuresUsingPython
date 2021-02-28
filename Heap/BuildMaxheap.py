class Heap:

    def heapify(self,arr,n,i):
        """

        :param arr: the input array
        :param n: size of the array
        :param i:  largest element of the heap
        :return: None
        """

        largest = i # starting from the last internal node
        left = 2 * i  +1
        right = 2 * i  + 2

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

arr = [4,1,3,2,16,9,10,14,8,7]
print("Before Max heap operation " , arr)

h = Heap()
h.buildmaxheap(arr,len(arr))
print("After operation ")
print(arr)


