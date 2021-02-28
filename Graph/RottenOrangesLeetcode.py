from collections import deque
# Contains Error .....

class Solution:
    def orangesRotting(self, grid):
        rows, cols = len(grid), len(grid[0])
        print(rows)
        print(cols)
        fresh_oranges = 0
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1

        directions = [(-1, 0), (0, 1), (1, 0), (0,-1)]
        time_taken = 0
        queue.append((-1, -1))

        print("Fresh Oranges Before Starting ", fresh_oranges)

        while queue:
            row, col = queue.popleft()

            if row == -1:
                time_taken += 1
                print("Time taken ", time_taken)
                if queue:
                    queue.append((-1, -1))


            else:
                for d in directions:  # For all of the neighbours of the current cell
                    n_row, n_col = row + d[0], col + d[1]  # moving in the all four directions of the current cell
                    print("Rows {} n_rows {} and cols {} and ncols {}".format(rows,n_row,cols,n_col))
                    print(rows > n_row >= 0 and cols > n_col >= 0)

                    if rows > n_row >= 0 and cols > n_col >= 0:

                        if grid[n_row][n_col] == 1:
                            print("Fresh Oranges "  , fresh_oranges)
                            grid[n_row][n_col] = 2
                            fresh_oranges -= 1
                            queue.append((n_row, n_col))

        print("Fres Oranges when Finished ", fresh_oranges)
        return time_taken if fresh_oranges == 0 else -1


s = Solution()
print(s.orangesRotting([[1, 2]]))
