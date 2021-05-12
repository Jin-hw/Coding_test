# n = input()

# result = []
# cut = ''
# a = []
# count_cutting = 0
# count_array = 1
# save = []
# seperate = []
# namerge = []

# for i in range(1, len(n)//2 + 1):
#     for t in n:
#         cut += t
#         count_cutting += 1
#         if count_cutting == i:
#             a.append(cut)
#             count_cutting = 0
#             cut = ''

#     cut = ''
#     count_cutting = 0

#     for u in range(i*(len(n)//i), len(n)):
#         namerge.append(n[u])

#     for k in range(1, len(a)):
#         if a[k] == a[k-1]:
#             count_array += 1
#         else:
#             if count_array != 1:
#                 result.append(str(count_array))
#             result.append(a[k-1])
#             count_array = 1
#     if count_array != 1:
#         result.append(str(count_array))

#     result.append(a[k])
#     # print(result)
#     for s in result:
#         # print(s)
#         if len(s) > 1:
#             for num in range(i):
#                 # print(num)
#                 seperate.append(s[num])
#         else:
#             seperate.append(s)
#     seperate = seperate + namerge
#     # print(seperate)
#     save.append(seperate)
#     seperate = []
#     result = []
#     a = []
#     namerge = []
#     count_array = 1


# small = 1001
# for i in save:
#     if len(i) < small:
#         small = len(i)

# print(small)
# ---------------시간 초과----------------------

s = input()

answer = len(s)
for step in range(1, len(s)//2 + 1):
    compressed = ""
    prev = s[0:step]
    count = 1

    for j in range(step, len(s), step):
        if prev == s[j:j + step]:
            count += 1
        else:
            compressed += str(count) + prev if count >= 2 else prev
            prev = s[j:j+step]
            count = 1
    compressed += str(count) + prev if count >= 2 else prev
    answer = min(answer, len(compressed))

print(answer)
