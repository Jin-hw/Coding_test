n = int(input())

load = list(map(str, input().split()))

now = [1, 1]

for i in load:
    if i == 'R':
        if now[1] < n:
            now[1] += 1
    elif i == 'L':
        if now[1] > 1:
            now[1] -= 1
    elif i == 'U':
        if now[0] > 1:
            now[0] -= 1
    elif i == 'D':
        if now[0] < n:
            now[0] += 1

for i in now:
    print(i, end=" ")
