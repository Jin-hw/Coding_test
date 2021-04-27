s = input()
num = ['-1'] * 26

for i in range((len(s))):
    if num[ord(s[i]) - ord('a')] == '-1':
        num[ord(s[i]) - ord('a')] = str(i)

print(" ".join(num))

# ----------------↑문자열 ↓ 숫자-------------------------

# s = input()
# num = [-1] * 26

# for i in range((len(s))):
#     if num[ord(s[i]) - ord('a')] == -1:
#         num[ord(s[i]) - ord('a')] = i

# for i in range(26):
#     print(num[i], end=" ")
