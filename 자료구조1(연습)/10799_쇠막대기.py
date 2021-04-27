pipe = list(input())
value = 0
answer = 0

for i in range(len(pipe)):
    if pipe[i] == '(':
        value += 1

    else:
        if pipe[i-1] == '(':
            value -= 1
            answer += value
        else:
            value -= 1
            answer += 1

print(answer)
