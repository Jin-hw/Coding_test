n = str(input())
array = []
for i in n:
    array.append(i)

first = len(array)//2
second = len(array)

sum_first = 0
sum_second = 0

for i in range(first):
    sum_first += int(array[i])
for i in range(first, second):
    sum_second += int(array[i])

if sum_first == sum_second:
    print('LUCKY')
else:
    print('READY')
