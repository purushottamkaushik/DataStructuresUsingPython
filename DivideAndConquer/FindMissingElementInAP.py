#
# def findmissingElement(arr) :
#     n = len(arr)
#     n1 = [0] * (n+1)
#     d = 2
#     for i in range(len(n1)):
#         n1[i] = d * i
#
#     for i in range(len(n1)):
#         if n1[i] not in arr:
#             print(n1[i])

# Order of N Solution
# def findmissingElement(arr):
#     d = 2
#     for i in range(len(arr)):
#         if arr[i] != arr[0] + d * i:
#             return arr[0] + d * i

arr = [0,2,4,6,10,12,14]

def findmissingElement(A,min,max ,d):

    if min > max:
        raise ValueError("min cannot be greater than max")
    mid = (min + max) // 2

    if min == max and A[min] != A[0] + d * min:
        return A[0] + d * min

    if A[mid] == A[0] * d * mid:
        min = mid +1
    else:
        max = mid - 1

    findmissingElement(A,min,max,d)

print(findmissingElement(arr,0,len(arr)-1,2))