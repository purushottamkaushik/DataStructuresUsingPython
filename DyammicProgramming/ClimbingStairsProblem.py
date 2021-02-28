
# def climbingStairs(n):
#
#     """This is a recursive formulation of Climbing stairs problem using top down Dyanmmic Programming"""
#
#     if n ==1 or n ==2:
#         return n
#     else:
#         return climbingStairs(n-1) + climbingStairs(n-2)



def climbingStairs(n):
    """This is a iterative implementation of the algorithm and uses the bottom up Dynammic Programming"""
    if n == 1 or n ==2:
        return n

    ways = 0
    for i in range(3,n+1):
        ways = climbingStairs(n-1) + climbingStairs(n-2)

    return ways

if __name__=="__main__":
    n = 6
    print(climbingStairs(n))
