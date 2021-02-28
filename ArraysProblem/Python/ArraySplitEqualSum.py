# def ArraySplit(A):
#     """This is a simple solution having time complexity O(n**2)"""
#
#     for i in range(len(A)):
#         leftsum = 0
#         rightsum = 0
#
#         for left in range(0,i+1):
#             leftsum +=A[i]
#
#         for right in range(i+1,len(A)):
#             rightsum +=A[i]
#
#         if rightsum == leftsum:
#             return len(A) -i
#
#     return -1


# def ArraySplit(A):
# """ THis is the optimal solution having time complexity O(n) """

#     sum = 0
#     for i in A:
#         sum +=i;
#     # print(sum)
#
#     sumhalfed = sum //2
#
#     # index = 0
#     for j in range(len(A)-1,-1,-1):
#         # print("J is " , j)
#         sum -=A[j]
#         print("sum is " , sum)
#         if sumhalfed == sum:
#              return j



# def ArraySplit(A):
#     """THis is also an Optimal Solution Of the above problem """
#     sum = 0
#     for i in range(len(A)):
#         sum +=A[i]
#
#
#     leftsum = sum
#     rightsum = 0
#
#     for j in range(len(A) - 1, -1 ,-1 ):
#         rightsum +=A[i]
#         leftsum -=A[i]
#
#         if (leftsum == rightsum):
#             return j
#
#     return -1
#
#
# print(ArraySplit([1,2,3,4,5,5]))
