n, k = map(int, input().split())

dp = [[0]*n for _ in range(k)]

for i in range(n):
    dp[0][i] = 1

for i in range(1, k):
    dp[i][0] = dp[i-1][0] + 1

for i in range(1, n):
    for j in range(1, k):
        dp[j][i] = dp[j-1][i] + dp[j][i-1]

print(dp[k-1][n-1] % 1000000000)

# 배열을 그려보면 간단하게 구할 수 있다.

# 11111111111
# 2345
# 36
# 4
# 5
