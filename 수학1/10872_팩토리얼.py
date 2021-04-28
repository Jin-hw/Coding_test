# import math

# n = int(input())

# answer = math.factorial(n)
# print(answer)

# -------------------------------
n = int(input())


def factorial(n):
    return n * factorial(n-1) if n > 1 else 1


print(factorial(n))
