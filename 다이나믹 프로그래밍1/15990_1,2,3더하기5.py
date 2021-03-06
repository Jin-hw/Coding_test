t = int(input())

d = [0] * 100001

s = [0] * 100000
a = [0] * 100000
f = [0] * 100000

d[1] = 1
d[2] = 1

s[0] = d[2]
a[0] = d[1]
f[0] = 1
d[3] = d[2] + d[1] + 1

s[1] = d[3] - s[0]
a[1] = d[2] - a[0]
f[1] = d[1]
d[4] = s[1] + a[1] + f[1]

s[2] = d[4] - s[1]
a[2] = d[3] - d[1]
f[2] = d[2]
d[5] = s[2] + a[2] + f[2]

for j in range(6, 100001):
    s[j-3] = (d[j-1] - s[j-4]) % 1000000009
    a[j-3] = (d[j-2] - a[j-5]) % 1000000009
    f[j-3] = (d[j-3] - f[j-6]) % 1000000009
    d[j] = s[j-3] + a[j-3] + f[j-3]

for _ in range(t):
    n = int(input())
    print(d[n] % 1000000009)

# ------------------------첫번쨰 방법--------------------------------------------

# dp = [[0]*4 for _ in range(100001)]
# dp[1][1] = 1
# dp[2][2] = 1
# dp[3][1], dp[3][2], dp[3][3] = 1, 1, 1

# for k in range(t):
#     n = int(input())
#     for i in range(4, n + 1):
#         for j in range(1, 4):
#             dp[i][j] = (((dp[i-j][1] + dp[i-j][2]) % 1000000009 +
#                          dp[i-j][3]) % 1000000009 - dp[i-j][j]) % 1000000009

#     print(((dp[n][1] + dp[n][2]) % 1000000009 + dp[n][3]) % 1000000009)

# #--------------------시간 초과---------------------------------------------------.

# dp = [[0]*4 for _ in range(100001)]
# dp[1][1] = 1
# dp[2][2] = 1
# dp[3][1], dp[3][2], dp[3][3] = 1, 1, 1

# for i in range(4, 100001):
#     for j in range(1, 4):
#         dp[i][j] = ((dp[i-j][1]+dp[i-j][2]) % 1000000009 +
#                     dp[i-j][3]) % 1000000009 - dp[i-j][j]

# for _ in range(t):
#     n = int(input())
#     print(((dp[n][1]+dp[n][2]) % 1000000009+dp[n][3]) % 1000000009)
