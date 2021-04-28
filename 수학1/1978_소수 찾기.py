n = int(input())

num = list(map(int, input().split()))
count = 0

for i in range(n):
    gong = 0
    if num[i] > 1:
        for k in range(2, num[i]):
            if num[i] % k == 0:
                gong += 1
        if gong == 0:
            count += 1
print(count)
