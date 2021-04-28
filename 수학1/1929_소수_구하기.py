# num1, num2 = map(int, input().split())

# for i in range(num1, num2):
#     gong = 0
#     if i > 1:
#         for k in range(2, int(i**0.5)+1):
#             if i % k == 0:
#                 gong += 1
#                 break
#         if gong == 0:
#             print(i)
# -----------------시간 초과--------------------
# def isPrime(num):
#     if num == 1:
#         return False
#     else:
#         for i in range(2, int(num**0.5)+1):
#             if num % i == 0:
#                 return False
#         return True


# M, N = map(int, input().split())

# for i in range(M, N+1):
#     if isPrime(i):
#         print(i)
# ---------------------------------------
m, n = map(int, input().split())

prime_list = [True] * (n + 1)
x = int((n + 1) ** 0.5)

for i in range(2, x + 1):
    if prime_list[i] == True:
        for j in range(i + i, n + 1, i):
            prime_list[j] = False


sieve = [i for i in range(2, n + 1) if prime_list[i] == True]

for i in range(len(sieve)):
    if sieve[i] >= m:
        print(sieve[i])
