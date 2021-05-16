n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
count = 0
while True:
    if min(a) < max(b):
        a[a.index(min(a))], b[b.index(max(b))
                              ] = b[b.index(max(b))], a[a.index(min(a))]
    else:
        break
    count += 1
    if count == k:
        break

print(a)
print(b)
print(sum(a))
