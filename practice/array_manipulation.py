def array_manipulation(arr, row):

    start_index, end_index, number_to_insert = row

    for i in range(start_index, end_index+1):
        arr[i-1] += number_to_insert

    return max(arr)


size_array = list(map(int, input().split()))
number_operations = size_array.pop(-1)

array = [0] * size_array[0]
max_numbers = []

for _ in range(number_operations):
    max_n = array_manipulation(array, list(map(int, input().split())))
    max_numbers.append(max_n)

print(max(max_numbers))

