# a = int(input())
# count = 0
# minimum = [a]


# def cal(a):
#     list = []
#     for i in a:
#         list.append(i-1)
#         if i % 3 == 0:
#             list.append(i//3)
#         if i % 2 == 0:
#             list.append(i//2)
#     print(list)
#     return list


# while True:
#     if a == 1:
#         print(count)
#         break
#     temp = minimum[:]
#     minimum = []
#     minimum = cal(temp)
#     count += 1
#     if min(minimum) == 1:
#         print(count)
#         break

n = int(input())
d = [0]*(n+1)
for i in range(2, n+1):
    d[i] = d[i-1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
print(d[n])
