n, x = map(int, input().split())

price = list(map(int, input().split()))

pages = list(map(int, input().split()))



"""
Main problem: In a set of n books, we have to find the maximum pages we can pick with at most price x
Sub problem: We will find the the maximum pages with price 1 to x for each prefix array from 1 to n. For each book, we can either pick it or not pick it
Base problem: For prefix array of size 0, the maximum pages we can pick will be 0
State: dp[i][w] -> Maximum pages we can have for prefix array of length i with max price w
Transition: Maximum of pick or not pick of a book
for eg: n=4 x=10
price = 4 8 5 3
pages = 5 12 8 1

Answer will be 13 (5 + 8)
"""

dp = []

for i in range(n+1):
    dp.append([0] * (x+1))
    
    
for i in range(1, n+1):
    for j in range(1, x+1):
        if j - price[i-1] >= 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-price[i-1]] + pages[i-1])
        else:
            dp[i][j] = dp[i-1][j]
    
    
print(dp[n][x])