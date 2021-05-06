n = int(input())

dp = [[0]*101 for _ in range(11)]

for i in range(10):
    dp[i][0] = 1

for i in range(1, 101):
    for j in range(10):
        if j == 0:
            dp[j][i] = (dp[j+1][i-1]) % 1000000000
        elif j == 9:
            dp[j][i] = (dp[j-1][i-1]) % 1000000000
        else:
            dp[j][i] = (dp[j-1][i-1] + dp[j+1][i-1]) % 1000000000

p = 0
for i in range(1, 10):
    p += dp[i][n-1]

print(p % 1000000000)
