

#
# def Leaders (A):
#     """
#     Brute Force way to find leaders in an array
#     :param A:
#     :return:
#     """
#
#     for i in range((len(A))):
#         for j in range(i+1,len(A)):
#             if A[j] > A[i]:
#                 # print(A[i] ," is not a leader ")
#                 break;
#
#         if j == (len(A) -1):
#             print(A[i] , " is a Leader")
#
#     return ""

def Leaders(A):
    max = -111111
    for i in range(len(A)-1,-1,-1):
        if A[i] > max:
            print(A[i] , " is a Leader")
            max = A[i]

print(Leaders([8,4,2,1,3,5,4,2]))


