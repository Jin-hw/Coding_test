import sys
while True:
    n = sys.stdin.readline().rstrip('\n')
    upper, lower, num, space = 0, 0, 0, 0

    if not n:
        break

    for i in n:
        if i.islower():
            lower += 1
        elif i.isupper():
            upper += 1
        elif i.isnumeric():
            num += 1
        else:
            space += 1

    print(lower, upper, num, space)
