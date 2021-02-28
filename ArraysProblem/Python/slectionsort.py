

def selection(arr) :

    for i in range(len(arr)):
        minindex = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[minindex]:
                minindex = j

        arr[i] , arr[minindex] = arr[minindex] , arr[i]



nums = [23,21,1,2,54,43,7]
print("before sorting " , nums)
selection(nums)
print("After sorting " , nums)

