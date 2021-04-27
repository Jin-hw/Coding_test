n = list(map(int, input().split()))

num_1 = ''
num_2 = ''
for i in range(len(n)):
    if i < 2:
        num_1 += str(n[i])
    else:
        num_2 += str(n[i])

print(int(num_1) + int(num_2))
