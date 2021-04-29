n = int(input(), 8)
answer = ''

while True:
    answer += str(n % 2)
    n = int(n / 2)
    if n == 1:
        answer += '1'
        break

for i in answer[::-1]:
    print(i, end="")
# -------------런타임에러---------------------
# print(bin(int(input(), 8))[2:])
