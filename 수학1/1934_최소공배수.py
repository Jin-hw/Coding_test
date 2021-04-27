num = int(input())

for i in range(num):
    n = list(map(int, input().split()))

    a = max(n[0], n[1])
    b = min(n[0], n[1])
    A = a
    B = b

    while True:
        if b != 0:
            if a % b == 0:
                ans = b
                break
            else:
                a_1 = b
                b_1 = a % b
                a = a_1
                b = b_1
        else:
            ans = a
            break

    c = A*B/ans

    print(int(c))
