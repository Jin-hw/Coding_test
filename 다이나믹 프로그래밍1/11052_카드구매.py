n = int(input())

p = list(map(int, input().split()))

d = [0] * (n+1)

d[0] = p[0]
for i in range(1, n):
    for j in range(i+1):
        if j == i:
            d[i] = max(d[i], p[i])
        d[i] = max(d[i], d[i-1-j] + p[j])
print(d[n-1])
