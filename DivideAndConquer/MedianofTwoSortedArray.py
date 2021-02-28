#
# def medianofsortedarray(arr1,arr2):
#     n = len(arr1)
#     m = len(arr2)
#     newarray = [0] * (m+n)
#     count = 0
#     i = j = 0
#     while i < n and j < m:
#         if arr1[i] <=arr2[j]:
#             newarray[count] = arr1[i]
#             count +=1
#             i +=1
#         else:
#             newarray[count] = arr2[j]
#             count +=1
#             j +=1
#
#     while i < n:
#         newarray[count] = arr1[i]
#         count +=1
#         i +=1
#
#     while j < m:
#         newarray[count] = arr2[j]
#         count +=1
#         j +=1
#
#     l1 = len(newarray)
#     print(" L1 is " , l1)
#     print(newarray)
#     if l1 % 2 != 0 :
#         return newarray[l1//2]
#
#     return (newarray[l1//2] + newarray[l1// 2 + 1]) / 2

def medianofsortedarray(arr1,arr2):
    n = len(arr1) + len(arr2)
    print(n)
    l1 = len(arr1)
    l2 = len(arr2)

    i = j = count = 0
    while i < l1 and j < l2 and count < n//2:
        if arr1[i] <=arr2[j]:
            i +=1
        else:
            j +=1
        count +=1

    


arr1 = [1,3,4,5,6,7,8,9,11]
arr2 = [1,4,6,8,12,14,15,17]
print(medianofsortedarray(arr1,arr2))