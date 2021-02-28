def CoinChange(C,A):

    """
    This is the problem of generating a amount by collecting minimum number of coins
    :param C:  Here c refers to the coins array . For example [1,2,5] that is the denominations we have of coins
    :param A: the amount you need to generate
    :return: number of coins
    """

    import sys
    N = [i for i in range(amount + 1)] # the array which contains N[0...... Amount]

    for i in range(1,len(N)):
        N[i] = sys.maxsize
    #
    # for i in range(1,amt+1):
    #     for j in range(m):
    #         if arr[j]<=i:
    #             temp=dp[i-arr[j]]
    #         if temp+1<dp[i]:
    #             dp[i]=temp+1

    for i in range(1,A+1):  # for every amount
        for j in range(len(C)): # for every coin
            if C[j] <= i :
                N[i] = min(N[i] ,N[i- C[j]] + 1)  # minimum of Cost of amount using coins

    return N[A]



if __name__=="__main__":
    coins = [1,2,5]
    amount = 2
    print(CoinChange(coins,amount))