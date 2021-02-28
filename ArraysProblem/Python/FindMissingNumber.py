
# def findMissing(a,n):
#
#     sum = (n * (n+1)) /2
#     # print("Sum is " ,sum)
#     array_sum = 0
#     for i in range(len(a)):
#         array_sum +=a[i]
#
#     # print("Array Sum " , array_sum)
#     return int(sum - array_sum)
#

#
# def findMissing(a,n):
#
#     """
#     This is a Function used to find missing number
#     """
#     num = 0
#     for i in range(1,n+1):
#         if i in a:
#             continue
#         else:
#             num = i
#
#     return num


def findMissing(a,n):
    x1 = a[0]
    for i in range(1,n-2):
        x1 = x1 ^ a[i]

    x2 = 0

    for j in range(n):
        x2 = x2 ^ j

    return x2 ^ x1

a = [ 1,2,4,3,6,7,9,8,10]
n = 10
print(n)

print("The Missing Number is  " , findMissing(a,10))



