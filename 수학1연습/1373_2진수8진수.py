n = list(map(int, input()))

n.reverse()

if len(n) % 3 == 2:
    n.append(0)
elif len(n) % 3 == 1:
    n.append(0)
    n.append(0)


answer = []
num = 0
count = 1

for i in n:
    if count == 1:
        if i == 0:
            num += 0
        else:
            num += 1
    elif count == 2:
        if i == 0:
            num += 0
        else:
            num += 2
    elif count == 3:
        if i == 0:
            num += 0
            count = 0
            answer.append(num)
            num = 0
        else:
            num += 4
            count = 0
            answer.append(num)
            num = 0
    count += 1

answer.reverse()

for i in answer:
    print(i, end="")

# -----------------------------
print(oct(int(input(), 2))[2:])
# int("11001100", 2) -> 204
# oct(204) -> Oo314
# Oo314[2:] -> 314
