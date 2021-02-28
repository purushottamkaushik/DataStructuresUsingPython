

def BrickFilling(n):

    """
    This is Problem which fills N*4 wall with 1*4 bricks
    this is the recursive solution of the problem
    :param n is the one dimension of the wall may be width or height
    :return the number of ways you can put bricks on the wall
    """

    if n==0 or n == 1 or n == 2 or n == 3 :
        return 1

    else:
        return BrickFilling(n-1) + BrickFilling(n-4)


if __name__=="__main__":
    n =5
    print("Using recurison" , BrickFilling(n))


def BrickFillingDP(n):

    """
    this is a function to implement brick filling problem using dynamic programming (Using bottom up Approach)
    :param n: is the one of the dimensions of the wall
    :return: integer : number of ways to fill the wall with the bricks

    """
    table = [0] *(n+1)
    # print(table)

    for i in range(0,4):
        table[i] = 1

    # print(table)

    for j in range(4,n+1):
        table[j] = table[j-1] + table[j-4]

    return table[n]



if __name__=="__main__":
    n =5
    print("Using recursive DP approach " , BrickFillingDP(n))
