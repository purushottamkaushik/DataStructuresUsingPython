


def countnegative(grid):
    n = len(grid)
    count = 0
    for row in range(n):
        for column in range(len(grid[row])):
            if grid[row][column] < 0:
                count += 1
    return count

grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]

print(countnegative(grid))