# def ArrayInversion (A):
#     count = 0
#     for i in range(len(A)):
#         for j in range(i+1,(len(A))):
#             if A[i] > A[j]:
#                 count +=1
#     return count
# a = [1,2,6,4,5]
# print(ArrayInversion(a))
############################################################################
def MergeSort(A,p,r):
    inversioncount = 0
    if p < r:
        q = (p+r) //2
        inversioncount +=  MergeSort(A,p,q)
        inversioncount +=  MergeSort(A,q+1,r)
        inversioncount +=  Merge(A,p,q,r)

    return inversioncount

def Merge(A,low,mid,high):
    temp = [0] * len(A)
    i = low
    j = mid + 1
    k = low

    count = 0
    # for i in range(len(A)):
    #     temp[k] = A[i]
    #     i +=1
    #     k +=1


    while i <= mid and j <=high:
        if A[i] > A[j]:
            count +=(mid - i + 1)
            temp[k] = A[j]
            j +=1
            k +=1
        else:
            temp[k] = A[i]
            i +=1
            k +=1

    while i <= mid:
        temp[k] = A[i]
        i +=1
        k +=1

    while  j <=high:
        temp[k] = A[j]
        j +=1
        k +=1

    #
    # for x in range(low ,len(A) -2):
    #     A[x] = temp[x]
    return count

a = [1,3,5,10,2,6,8,9]
print(MergeSort(a,0,(len(a) -1)))
