
def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j] ,arr[j+1] = arr[j+1] , arr[j]

arr = [1,10,2,12,5]
print(arr)
bubblesort(arr)
print(arr)