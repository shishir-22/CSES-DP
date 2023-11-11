n, x = map(int, input().split())
coins = list(map(int, input().split()))


"""
Main problem: Find all possible ways to obtain sum x using given coins
Sub problem: Find all possible ways to obtain sum k-c1, k-c2, k-c3 .... k-cn. (These can further be divied into subproblems)
Base problem: For sum 0, we can have only 1 ways that is not using any coins
State: dp[k] Total number of ways to obtain sum k
Transition: For any k, sum of all possible ways to obtain k-c1, k-c2, k-c3 .... k-cn.
    
for eg: for n=3 x=9 and coins = [2,3,5]. Total number of ways to obtain x=9 is 8

9 -> 9 - 2 / 9 - 3 / 9 - 5

9 - 2 = 7 -> 7 - 2 / 7 - 3 / 7 - 5

9 - 3 = 6 -> 6 - 2 / 6 - 3 / 6 - 5

9 - 5 = 4 -> 4 - 2 / 4 - 3 / 4 - 5

4 - 2 = 2 -> 2 - 2 = 0 (One possible way: 5, 2, 2)


"""

dp = [0] * (x+1)
dp[0] = 1

for i in range(x+1):
    for c in coins:
        if i - c >= 0:
            dp[i] = (dp[i - c] + dp[i]) % 1000000007
           
print(dp[x])