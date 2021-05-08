import math

n = int(input())
count = 0

dp = [0 for i in range(n + 1)]
square = [i * i for i in range(1, 317)]
for i in range(1, n + 1):
    s = []
    for j in square:
        if j > i:
            break
        s.append(dp[i - j])
    dp[i] = min(s) + 1
print(dp[n])

while n != 0:
    n = n-int(math.sqrt(n))**2
    print(n)
    count += 1

print(count)
