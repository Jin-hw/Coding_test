n = input()
num = [0] * 26
print(num)
for i in n:
    num[ord(i) - ord('a')] += 1

for i in range(26):
    print(num[i], end=" ")
