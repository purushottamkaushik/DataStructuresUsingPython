class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[1] * n for _ in range(m)]  # Creating a n*m grid
        
        for col in range(1,m): # iterating over the columns 
            for row in range(1,n): # iterating over the row
                dp[col][row] = dp[col-1][row] + dp[col][row-1]
        
        return dp[m-1][n-1] 

        
        