n = str(input())

alphabet = 'abcdefghijklmnopqrstuvwxyz'
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

answer = ''
for i in n:
    if i in alphabet:
        if ord(i) < 110:
            answer += chr(ord(i)+13)
        else:
            answer += chr(ord(i)-13)
    elif i in ALPHABET:
        if ord(i) < 78:
            answer += chr(ord(i)+13)
        else:
            answer += chr(ord(i)-13)
    else:
        answer += i

print(answer)
