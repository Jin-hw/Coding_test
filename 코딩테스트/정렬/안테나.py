n = int(input())
a = list(map(int, input().split()))
a.sort()

# sum_array = []
# for i in range(n):
#     sum_num = 0
#     for j in range(n):
#         sum_num += abs(a[i] - a[j])
#     sum_array.append(sum_num)

# print(a[sum_array.index(min(sum_array))])

print(a[(n-1)//2])
