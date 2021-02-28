
# Dynamic Programming Approach
import sys
def EggBreak(n,k):

    table = [[  sys.maxsize  for column in range(k+1)] for row in range(n+1)]

    for col in range(1,k+1):

        table[1][col] = col

    for row in range(1,n+1):
        table[row][1] = 1

    for i in range(2,n+1): # for number of eggs
        for j in range(2,k+1): # for number of floors in the building
            for x in range(1,j+1):
                table[i][j] = min(table[i][j] , 1 + max(table[i-1][x-1] , table[i][j-x]))

    #
    # for i in range(2, n + 1):
    #     for j in range(2, k + 1):
    #         table[i][j] = sys.maxsize
    #         for k in range(1, j + 1):
    #             temp = 1 + max(table[i - 1][k - 1], table[i][j - k])
    #             table[i][j] = min(temp, table[i][j])

    print("Updated Table ")
    for t in table:
        print(t)

    return table[n][k]



if __name__=="__main__":
    n = 2
    k = 10
    print(EggBreak(n,k))

    # recursive Approach
import sys


# def eggDropsRecursion(eggs, floor):
#     if floor == 0 or floor == 1:
#         return floor
#     if eggs == 1:
#         return floor
#     minvalue = sys.maxsize
#
#     for i in range(1, floor + 1):
#         temp = max(eggDropsRecursion(eggs - 1, i - 1), eggDropsRecursion(eggs, floor - i))
#         if temp < minvalue:
#             minvalue = temp
#
#     return minvalue + 1
#
#
# if __name__ == '__main__':
#     print(eggDropsRecursion(2, 10))