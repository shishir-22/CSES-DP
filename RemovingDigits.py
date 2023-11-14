n = int(input())

"""
Main problem: Find the steps required to make the given number(n) 0 by subtracting the digits from number in one step
Sub problem: For number n(d1d2d3....dn), find the steps required to make n-d1, n-d2, n-d3 .... n-dn (These may have further sub problems)
Base problem: For number 0, 0 steps are required to subtract digits
State: dp[k] -> Number of steps required to reach 0 for number k
Transition: For number k, minimum of steps required for k-d1, k-d2, k-d3.....k-dk 
    
for eg: n = 27

27 -> 27 - 2 / 27 - 7

25 -> 25 - 2 / 25 - 5

20 -> 20 - 2

23 -> 23 - 2 / 23 - 3

so on...

"""


INT_MAX = 1000000000
dp = [INT_MAX] * (n + 1)

dp[0] = 0

for i in range(1, n + 1):
    for digit in str(i):
        if int(digit) != 0:
            dp[i] = min(dp[i], dp[i - int(digit)] + 1)
            
print(dp[n])
    