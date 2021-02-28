def selection(arr):

    for i in range(len(arr)):
        min = i
        for j in range(min,len(arr)):
            if arr[j] < arr[min]:
                min = j

        arr[min] , arr[i] = arr[i] ,arr[min]


arr = [54, 26, 93, 17, 77,31, 44, 55]
print(arr)
selection(arr)
print(arr)
