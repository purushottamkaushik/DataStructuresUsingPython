

#recursive approach

def RodCuttingProblem(P,n):
    # if the length of rod is zero then the revenue generated will be zero
    if n <= 0 :
        return 0

    best = -1

    # this is the recursive case of the problem where the rod is cutted into pieces and revenue is measured
    for i in range(n):
        best = max(best , P[i] + RodCuttingProblem(P,n-(i+1)))

    return best

if __name__=="__main__":
    pricelist = [2, 3, 7, 8, 9]
    n = 5
    print("Max Revenue " , RodCuttingProblem(pricelist,n))




# Using dynammic programming
# def RodCuttingProblem(P,n):
#
#     dp = [0] * (n)
#     dp[0] = 0
#
#     for i in range(1,n): #  length of rod to be cut
#         best = -1
#         for j in range(1,i): # loop for calculating the best price
#             best = max(best, P[i] + dp[j -(i+1)] )
#         dp[i] = best
#     print(dp)
#
#     return dp[n-1]


if __name__=="__main__":
    pricelist = [2, 3, 7, 8, 9]
    n = 5
    print("Max Revenue " , RodCuttingProblem(pricelist,n))

