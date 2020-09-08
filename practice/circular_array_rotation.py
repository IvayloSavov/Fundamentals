def circular_array_rotation(info: list, arr: list, queries_to_print: list):
    rotation_count = info[1]
    for _ in range(rotation_count):
        element_to_remove_and_insert_then = arr.pop(-1)
        arr.insert(0, element_to_remove_and_insert_then)

    numbers_to_print = []
    for index in queries_to_print:
        numbers_to_print.append(arr[index])

    numbers_to_print = list(map(str, numbers_to_print))
    return "\n".join(numbers_to_print)


data = list(map(int, input().split()))
array = list(map(int, input().split()))
queries = []

for _ in range(data[2]):
    query = int(input())
    queries.append(query)

print(circular_array_rotation(data, array, queries))