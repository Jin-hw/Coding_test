n = input()

mark = '-'
array = []
result = ''

for i in range(len(n)):
    if n[i] == '<':
        mark = '+'
        while array:
            result += array.pop()
        result += '<'
    elif n[i] == '>':
        array.append(n[i])
        mark = '-'
        array.reverse()
        while array:
            result += array.pop()
    elif n[i] == " ":
        if mark == '+':
            array.append(n[i])
            array.reverse()
            while array:
                result += array.pop()
        elif mark == '-':
            while array:
                result += array.pop()
            result += ' '
    else:
        array.append(n[i])

while array:
    result += array.pop()

print(result)
