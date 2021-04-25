n = int(input())

data = list(map(int, input().split()))
result = [-1 for _ in range(n)]
print(result)
stack = []
signal = '0'

for i in range(n):
    for j in range(i, n):
        if data[i] < data[j]:
            stack.append(data[j])
            signal = '-'
            break
        elif data[i] >= data[j]:
            signal = '+'
    if signal == '+':
        stack.append(-1)
        signal = '-'

for i in range(n):
    print(stack[i], end=" ")
