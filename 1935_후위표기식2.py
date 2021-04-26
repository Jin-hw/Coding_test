n = int(input())

res = list(map(str, input()))
num = []

for i in range(n):
    n = int(input())
    num.append(n)

stack = []

for i in res:
    if i.isalpha():
        stack.append(num[ord(i) - ord('A')])
    else:
        str2 = stack.pop()
        str1 = stack.pop()

        if i == '+':
            stack.append(str1 + str2)
        elif i == '-':
            stack.append(str1 - str2)
        elif i == '*':
            stack.append(str1 * str2)
        elif i == '/':
            stack.append(str1 / str2)

print(f"{stack[0]:.2f}")
