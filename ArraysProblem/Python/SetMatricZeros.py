def setZeros(matrix):
    n = len(matrix)
    rows = []
    columns = []

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                rows.append(i)
                columns.append(j)
    print(rows)
    print(columns)

    for i in rows:
        for j in range(len(matrix[i])):
            matrix[i][j] = 0


    for row in range(len(matrix)):
        for col in columns:
            matrix[row][col] = 0

    print(matrix)


input = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
setZeros(input)
