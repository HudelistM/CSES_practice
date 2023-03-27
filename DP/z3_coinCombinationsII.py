n, x = map(int, input().split())
coins = [int(x) for x in input().split()]
dp = [0] * 1000001
dp[0] = 1
MOD = 10**9 + 7
for i in range(1, n + 1):
    for weight in range(x + 1):
        if weight - coins[i - 1] >= 0:
            dp[weight] += dp[weight - coins[i - 1]]
            dp[weight] %= MOD
print(dp[x])
