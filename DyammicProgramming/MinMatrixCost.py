def MinCostMatrix(m,n):

    costmat = [ [ 0 for k in range(n)] for j in range(m)]
    print(costmat)

    for i in range(len(matrix[0])):
        costmat[0][i] = costmat[0][i-1] + matrix[0][i]

    print(costmat)

    for j in range(len(matrix)):
        costmat[j][0] = matrix[j][0] + costmat[j-1][0]

    for row in range(1,len(matrix)):
        for column in range(1,len(matrix[row])):
            costmat[row][column] = matrix[row][column] + min(costmat[row][column-1],costmat[row-1][column])

    print(costmat)
    return costmat[m-1][n-1]
    # return "hello"


if __name__=="__main__":
    matrix = [[2,1,5,1],[3,4,2,2],[1,2,3,3],[1,3,2,4]]
    m = len(matrix)
    n = len(matrix[0])
    print(MinCostMatrix(m,n))



