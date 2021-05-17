n = int(input())
stages = list(map(int, input().split()))


# count = [0] * (max(stages) + 1)

# for i in range(len(stages)):
#     count[stages[i]] += 1
# rate = []

# for i in range(1, n + 1):
#     rate.append((i, count[i] / (sum(count)-sum(count[:i]))))

# rate.sort(key=lambda x: x[1], reverse=True)

# answer = [i[0] for i in rate]

# print(answer)

# -----------계수정렬 숫자가 적을 때------------------

answer = []
length = len(stages)

for i in range(1, n+1):
    count = stages.count(i)

    if length == 0:
        fail = 0
    else:
        fail = count/length

    answer.append((i, fail))
    length -= count

answer = sorted(answer, key=lambda x: x[1], reverse=True)

answer = [i[0] for i in answer]

print(answer)
