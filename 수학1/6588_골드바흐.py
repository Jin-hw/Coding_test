# def getPrimaryNum_Eratos(N):
#     nums = [True] * (N + 1)
#     for i in range(2, len(nums) // 2 + 1):
#         if nums[i] == True:
#             for j in range(i+i, N, i):
#                 nums[j] = False
#         return [[i for i in range(2, N) if nums[i] == True], nums]


# primary_nums = getPrimaryNum_Eratos(1000000)[0]
# primary_bools = getPrimaryNum_Eratos(1000000)[1]
# while(True):
#     N = int(input())
#     if N == 0:
#         break
#     for i in range(N // 2):
#         if primary_bools[N-primary_nums[i]] == True:
#             print("{} = {} + {}".format(N, primary_nums[i], N-primary_nums[i]))
#             break
# ---------------------------------------------------
import sys


def Goldbach():
    check = [False, False] + [True] * 1000000

    for i in range(2, 1001):
        if check[i] == True:
            for j in range(i + i, 1000001, i):
                check[j] = False

    while True:
        n = int(sys.stdin.readline())

        if n == 0:
            break

        A = 0
        B = n
        for _ in range(1000000):
            if check[A] and check[B]:
                print(f"{n} = {A} + {B}")
                break
            A += 1
            B -= 1
        else:
            print("Goldbach's conjecture is wrong.")


Goldbach()
