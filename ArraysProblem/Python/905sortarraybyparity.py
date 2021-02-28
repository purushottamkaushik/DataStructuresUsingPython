

# def sortArrayByParity(A) :
#     A = sorted(A)
#     evenlist = []
#     oddlist = []
#     for i in A:
#         if i %2 ==0 :
#             evenlist.append(i)
#         else:oddlist.append(i)
#
#     for i in oddlist:
#         evenlist.append(i)
#
#
#     print(evenlist)
#
#     return None


# def sortArrayByParity(A) :
#     return [ i for i in A if i%2 ==0] +  [ i for i in A if i%2 !=0]

def sortArrayByParity(A):
    i = 0
    j = len(A) - 1

    while i < j:
        if A[i] % 2 != 0:
            A[i], A[j] = A[j], A[i]
            j -= 1
        else:
            i += 1
    print(A)
    return A


nums = [3,1,2,4]
sortArrayByParity(nums)
