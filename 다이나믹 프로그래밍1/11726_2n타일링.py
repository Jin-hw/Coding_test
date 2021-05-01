n = int(input())

d = [0] * (n+1)  # 왜 인지 모르겠으나 백준에서 n으로 하면 인덱스 에러 생김
d[0] = 1
d[1] = 2

for i in range(2, n):
    d[i] = d[i-1] + d[i-2]

print(d[n-1] % 10007)
