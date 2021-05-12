n = input()

n = sorted(n)

alpha = []
number = []

for i in n:
    if i.isalpha() == True:
        alpha.append(i)
    else:
        number.append(i)

sum = 0
for i in number:
    sum += int(i)

alpha.append(str(sum))

for i in alpha:
    print(i, end="")

# print(''.join(alpha))
