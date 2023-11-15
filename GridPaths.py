n = int(input())

grid = []

for i in range(n):
    input_string = input()
    grid.append([])
    for j in input_string:
        grid[i].append(j)

"""
Main problem: For n * n grid, find all the paths to reach from (0,0) to (n-1,n-1)
Sub problem: For any i, j of n * n grid, find all the paths to reach from (i,j) to (n-1, n-1)
Base problem: Paths to reach from (n-1, n-1) to (n-1, n-1) will be 1
State: For any i,j, dp[i][j] will be the paths to reach from (i,j) to (n-1,n-1)
Transition:  For any i,j, sum of paths from (i+1,j)to (n-1,n-1) and (i, j+1) to (n-1,n-1)
    
for eg: n = 4 and grid = ....
                         .*..
                         ...*
                         *...
        
        Answer will be 3

"""

dp = []

for i in range(n + 1):
    dp.append([0] * (n + 1))
    
if grid[n-1][n-1] != "*":
    dp[n-1][n-1] = 1
else:
    # If last cell is marked as trap, then we have no way to reach
    print(0)
    exit()

MOD = 1000000007


for i in range(n - 1, -1, -1):
    for j in range(n - 1, -1, -1):
        if grid[i][j] != "*":
            dp[i][j] = 1 if (i+1 == n and j+1 == n) else (dp[i+1][j] + dp[i][j+1]) % MOD
    
print(dp[0][0])
    