n = int(input())
array_1 = list(map(int, input().split()))

m = int(input())
array_2 = list(map(int, input().split()))


def bainary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return bainary_search(array, target, start, mid - 1)
    else:
        return bainary_search(array, target, mid + 1, end)


for i in array_2:
    result = bainary_search(array_1, i, 0, n-1)
    if result == None:
        print("no", end=' ')
    else:
        print("yes", end=' ')
