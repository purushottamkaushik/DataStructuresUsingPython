


# def kthsmallest(arr,k):
#
#     for j in range(1,len(arr)):
#         key = arr[j]
#         i = j - 1
#
#         while i >= 0 and key < arr[i]:
#             arr[i+1] = arr[i]
#             i -=1
#         arr[i+1] = key
#     return arr[k-1]




class Heap:

    def heapify(self,arr,n,i):
        """

        :param arr: the input array
        :param n: size of the array
        :param i:  largest element of the heap
        :return: None
        """

        smallest = i # starting from the last internal node
        left = 2 * i  +1
        right = 2 * i  + 2

        if left < n and arr[i] > arr[left]:
            smallest = left

        if right < n and arr[smallest] > arr[right]:
            smallest = right

        if smallest != i :
            arr[smallest] , arr[i] = arr[i] , arr[smallest]
            self.heapify(arr,n,smallest)


    def buildminheap(self,arr,n):
        l = len(arr)
        for i in range(l//2,-1,-1):
            self.heapify(arr,l,i)

    def ksmallest(self,arr,n):
        k = n
        print(arr)
        self.buildminheap(arr,len(arr))
        print(arr)
        for i in range(k-1,0,-1):
            arr[i] ,arr[0] = arr[0] , arr[i]
            self.heapify(arr,len(arr),i)


arr = [13,12,11,14,15,17,18,20,19,16]
# print(kthsmallest(arr,4))
h = Heap()

h.ksmallest(arr,4)


