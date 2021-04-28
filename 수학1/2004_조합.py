# import math
# n, m = map(int, input().split())


# def factorial_created(n):
#     return n * factorial_created(n-1) if n > m else 1


# value = int(factorial_created(n)/math.factorial(n-m))
# str_value = str(value)
# stack = []
# for i in str_value:
#     stack.append(i)
# stack.reverse()
# for i in range(len(stack)):
#     if stack[i] != '0':
#         print(i)
#         break
# --------------------------------------

def countNum(N, num):
    count = 0
    divNum = num
    while(N >= divNum):
        count = count + (N // divNum)
        divNum = divNum * num  # num이 지수배로 증가해서 처음에는 num이 1개, 다음은 2개
    return count


M, N = map(int, input().split())

print(min(countNum(M, 5) - countNum(N, 5) - countNum(M-N, 5),
          countNum(M, 2) - countNum(N, 2) - countNum(M-N, 2)))
