# def partition(arr,p,r):
#     pivot = arr[p]
#     i = p
#
#     for j in range(p+1,r+1):
#         if arr[j] < pivot:
#             i +=1
#             arr[i] , arr[j] = arr[j] , arr[i]
#
#     arr[i] , arr[p] = arr[p] ,arr[i]
#     return i
#
#
#
# def quicksort(arr,p,r):
#     if p < r :
#         q = partition(arr,p,r)
#         quicksort(arr,p,q-1)
#         quicksort(arr,q+1,r)




























def partition(arr,p,r):
    pivot = arr[p] # chossing a pivot
    i = p # i is pointing to the pivot element
    for j in range(p+1,r+1):
        if arr[j] < pivot:
            i +=1
            arr[j] , arr[i] = arr[i] , arr[j]

    arr[i] ,arr[p] = arr[p] ,arr[i]
    return i


def quicksort(arr,p,r):
    if p < r:
        q = partition(arr,p,r)
        quicksort(arr,p,q-1)
        quicksort(arr,q+1,r)

arr = [54,12,43,34,56,72,11,10]
quicksort(arr,0,len(arr)-1)
print(arr)
