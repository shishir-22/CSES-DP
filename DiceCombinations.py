i = int(input())

def count_ways_to_get_sum_n(n):
    """
    Main problem: Find the number of ways to get sum n by throwing dice any number of times.
    Sub problem: Find the number of ways to get sum k by throwing dice. To reach to sum k, you can throw the dice and reach from k-1, k-2. k-3, k-4, k-5, k-6.
    Base problem: k=0, we know there is only 1 way to get sum 0 by not throwing dice.
    State: dp[k] Number of ways to get sum k by throwing dice any number of times
    Transition: For any k, sum of k - 1, k - 2, k - 3, k - 4, k - 5, k - 6 ways
    
    for eg: for K=3, sum of (3-1), (3-2) (3-3) ways // 2 + 1 + 1 = 4 ways
    for (3-1) = 2 = sum of (2-1), (2-2) ways // 2
    for (3-2) = 1 = sum of (1-1) ways // 1
    for 0 = 1 // base condition
    
    
    """
    dp = [1]
 
    for i in range(1, n + 1):
        dp.append(sum(dp[-6:]) % 1000000007)
                
    return dp[n]
    

print(count_ways_to_get_sum_n(i))