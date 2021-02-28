
# def RotateArrayKTimes(A,k):
#
#     """This is a Solution which follows O(n**2) time complexity"""
#     for k in range(k):
#         lastElement = A[len(A) - 1]
#
#         for j in range(len(A)-2,-1,-1):
#             A[j+1] = A[j]
#
#         A[0] = lastElement

# 2nd method
#
# def reverse(A,low, high):
#       """This is a function to reverse an array """
#     i = low
#     j = high
#     while(i < j):
#         A[i] , A[j] = A[j] , A[i]
#         i = i + 1 # increment i by 1
#         j = j - 1 # decrement j by 1
#
# def RotateArrayKTimes(lst,k):
          #  """This is function to rotate array K times with O(1) space and O(n) time """
#     n = len(lst)
#     k = k % n
#     reverse(lst,0,n-k-1)
#     reverse(lst,n-k,n-1)
#     reverse(lst,0,n-1)
#

#
# def RotateArrayKTimes(lst , k):
#
#     n  = len(lst)
#     temp = []
#
#     for i in range(n-k,n):
#         temp.append(lst[i])
#
#     print(temp)
#
#     for j in range(n-k):
#         lst[j+k] = lst[j]
#
#     print(lst)
#
#     for item in range(k):
#         lst[item] =  temp[item]
#
#     print(lst )



# lst =[1,2,3,4,5]
# RotateArrayKTimes(lst,3)
# print("Printing the rotated array" )
# print(lst)
