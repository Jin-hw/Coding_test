s = input()

count0 = 0
count1 = 0

for i in range(1, len(s)):
    if s[i] != s[i-1]:
        if s[i-1] == '1':
            count0 += 1
        else:
            count1 += 1

if s[-1] == '1':
    count0 += 1
else:
    count1 += 1

# if s[0] == '1':
#     count0 += 1
# else:
#     count1 += 1

# for i in range(len(s) - 1):
#     if s[i] != s[i+1]:
#         if s[i+1] == '1':
#             count0 += 1
#         else:
#             count1 += 1

result = 0
result = min(count0, count1)
print(result)
