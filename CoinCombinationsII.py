n, x = map(int, input().split())
coins = list(map(int, input().split()))


"""
Main problem: Find all possible distinct ordered ways to obtain sum x using given coins
Sub problem: Find all possible distinct ordered ways to obtain sum k - c1, k - c2, k - c3 .... k - cn in ordered way (Ordered way -> Looping over coins first so that the dp states will be calculated in order of coins)
Base problem: For sum 0, we can have only 1 ways that is not using any coins
State: dp[k] Total number of ways to obtain sum k in ordered way
Transition: For any k, sum of all possible ways to obtain k-ci, k-ci+1, k-ci+1 .... k-cn where i will range from i to n
    
for eg: for n=3 x=9 and coins = [2,3,5]. Total number of ways to obtain x=9 is 8

9 -> 9 - 2 / 9 - 3 / 9 - 5

9 - 2 = 7 -> 7 - 2 / 7 - 3 / 7 - 5

9 - 3 = 6 -> 6 - 3 / 6 - 5 // IMPORTANT: Since we have reached 6 by picking 3, now we can only pick 3 and 5 because we want to find ordered ways

9 - 5 = 4 -> 4 - 5 X // IMPORTANT: Since we have reached 4 by picking 5, now we can only pick 5 because we want to find ordered ways

7 - 2 = 5 -> 5 - 2 / 5 - 3 / 5 - 5

so on ............


Note: This is the space optimized way to implement this problem, there is another way to solve this problem with 2D DP where we have to maintain the state in dp[i][k] -> No of ways to acheive sum K using coins from i to n.
"""

dp = [0] * (x+1)
dp[0] = 1

for c in coins:
    for i in range(x+1):
        if i - c >= 0:
            dp[i] = (dp[i - c] + dp[i]) % 1000000007
           
print(dp[x])