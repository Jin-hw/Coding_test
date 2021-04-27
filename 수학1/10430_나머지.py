n = list(map(int, input().split()))

A = n[0]
B = n[1]
C = n[2]

print((A+B) % C)
print(((A % C)+(B % C)) % C)
print((A*B) % C)
print(((A % C)*(B % C)) % C)
