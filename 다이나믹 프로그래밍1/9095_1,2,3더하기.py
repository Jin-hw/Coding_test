n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

N = max(array)

d = [0] * (N + 1)

d[0] = 1
d[1] = d[0] + 1
d[2] = d[1] + d[0] + 1

for i in range(3, N):
    d[i] = d[i-1] + d[i-2] + d[i-3]


for i in array:
    print(d[i-1])
