def get_diagonal(arr):
    index = 0
    diagonal = []

    for row in arr:
        number = row[index]
        diagonal.append(number)
        index += 1

    return diagonal


def diagonal_difference(arr):
    first_diagonal = get_diagonal(arr)
    arr.reverse()
    second_diagonal = get_diagonal(arr)

    return abs(sum(first_diagonal) - sum(second_diagonal))


count_rows = int(input())
array = []

for _ in range(count_rows):
    row = list(map(int, input().split()))
    array.append(row)

print(diagonal_difference(array))