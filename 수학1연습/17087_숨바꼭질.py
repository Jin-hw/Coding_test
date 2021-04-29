def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


N, S = map(int, input().split())
location = list(map(int, input().split()))
distance = []
for i in location:
    distance.append(abs(i-S))

result = distance[0]

for idx in range(1, N):
    result = gcd(result, distance[idx])

print(result)

# 수빈이와 동생들의 각 거리를 뺀 숫자들의 최대공약수
