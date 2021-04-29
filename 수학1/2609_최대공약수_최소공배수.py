# n = list(map(int, input().split()))

# a = max(n[0], n[1])
# b = min(n[0], n[1])
# A = a
# B = b

# while True:
#     if b != 0:
#         if a % b == 0:
#             ans = b
#             break
#         else:
#             a_1 = b
#             b_1 = a % b
#             a = a_1
#             b = b_1
#     else:
#         ans = a
#         break

# c = A*B/ans

# print(ans)
# print(int(c))

# 유클리드 호제법
# --------------------------
n, m = map(int, input().split())

if m > n:
    n, m = m, n
N, M = n, m
while n % m != 0:
    n, m = m, n % m
print(m)

ans = N*M/m

print(int(ans))
