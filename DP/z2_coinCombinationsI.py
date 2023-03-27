MOD=1000000007
n, x = map(int, input().split())
coins = list(map(int, input().split()))

dp = [0 for i in range(1000001)]
dp[0] = 1
for weight in range(x+1):
    for i in range(1, n+1):
        if weight - coins[i - 1] >= 0:
            dp[weight] += dp[weight - coins[i - 1]]
            dp[weight] %= MOD
print(dp[x])

