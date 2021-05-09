n = int(input())

dp = [0 for i in range(n+1)]

for i in range(1, n+1):
    s = []
    for j in range(1, i+1):
        if j*j > i:
            break
        elif i >= j*j:
            s.append(dp[i-j*j])
    dp[i] = min(s) + 1

print(dp[n])

# https://pacific-ocean.tistory.com/205
