n = int(input())


def factorial(n):
    return n * factorial(n-1) if n > 1 else 1


value = factorial(n)
str_value = str(value)
stack = []
for i in str_value:
    stack.append(i)
stack.reverse()
for i in range(len(stack)):
    if stack[i] != '0':
        print(i)
        break
