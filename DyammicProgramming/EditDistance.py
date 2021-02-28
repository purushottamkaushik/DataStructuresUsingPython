

def EditDistance(X,y ,m,n):
    """
    THis is the recusrsive soultion of the Edit Distance problem
    :param X: THis is first String
    :param y: This is the second string
    :param m: This is the length of the first string

    :param n: This is the length of the second string
    :return: the edit distance (the number of characters change from second string to obtain first string)
    """

    if m == 0 : # if first string length is zero then return length of second string
        return n
    elif n == 0 : # if second string length is zero then return length of first string
        return m
    elif X[m-1] == y[n-1]: # if last character match then call the editdistance with excluding that character
         return EditDistance(X,y,m-1,n-1);
    else: # find minimum of the edit distance of insert , delete and matching character operation
        return 1 + min(EditDistance(X,y,m-1,n-1),EditDistance(X,y,m,n-1),EditDistance(X,y,m-1,n))



if __name__=="__main__":
    s1 = "abcdg"
    s2 = "abdefg"
    l1 = len(s1)
    l2 = len(s2)
    print(EditDistance(s1,s2,l1,l2))



# Dynamic prgramming approach

def EditDistance(X,y,m,n):

    print("N is " ,n)
    print("M is " , m)
    table = [[ 0 for j in range(m)] for i in range(n)]

    print("Initialzed table ")
    for p in table:
        print(p)

    for j in range(n):
        table[j][0] = j

    for i in range(m):
        table[0][i] = i
    print("New Table ")
    for t in table:
        print(t)

    for i in range(1,n):
        for j in range(1,m):
            if y[i] == X[j]:
                table[i][j] = table[i-1][j-1]
            else:
                table[i][j] = 1 + min(table[i-1][j-1],
                                      table[i-1][j],
                                      table[i][j-1]
                                      )
    print("Final TAble" )
    for t in table:
        print(t)

    return table[n-1][m-1]


if __name__ == "__main__":
    s1 = "abcdg"
    s2 = "abdefg"
    l1 = len(s1)
    l2 = len(s2)
    print(EditDistance(s1, s2, l1, l2))
