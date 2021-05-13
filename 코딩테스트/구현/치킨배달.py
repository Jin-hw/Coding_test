# m = [[0]*5 for i in range(5)]
# for i in range(5):
#     m[i] = list(map(int, input().split()))

# house = []
# chicken = []
# for i in range(5):
#     for j in range(5):
#         if m[i][j] == 1:
#             house.append([i+1, j+1])
#         if m[i][j] == 2:
#             chicken.append([i+1, j+1])


# answer_array_2 = []
# sum_distance = 0
# for i in chicken:
#     x_c, y_c = i
#     answer = 0
#     answer_array = []
#     for j in house:
#         x_h, y_h = j
#         answer = abs(x_c - x_h) + abs(y_c - y_h)
#         # print(answer)
#         answer_array.append(answer)
#     #print(x_c, y_c)
#     sum_distance += min(answer_array)
#     # print(sum_distance)

# print(sum_distance)

# --------------------------------------
from itertools import combinations

n, m = map(int, input().split())
chicken, house = [], []

for r in range(n):
    data = list(map(int, input().split()))

    for c in range(n):
        if data[c] == 1:
            house.append((r, c))
        elif data[c] == 2:
            chicken.append((r, c))

candidates = list(combinations(chicken, m))


def get_sum(candidate):
    result = 0
    for hx, hy in house:
        temp = 1e9
        for cx, cy in candidate:
            print(cx, cy)
            temp = min(temp, abs(hx-cx) + abs(hy-cy))
        print("---------------------")
        result += temp
    return result


result = 1e9
for candidate in candidates:
    print(candidate)
    result = min(result, get_sum(candidate))
    print("+++++++++++++++++++++++++++++++++++++++++")

print(result)
print(chicken)
print(candidates)
