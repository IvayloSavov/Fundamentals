def maximum_sum(arr: list):
    max_value = []
    current_max_array = arr.copy()
    while len(current_max_array) > 1:
        biggest_number = max(current_max_array)
        current_max_array.remove(biggest_number)
        max_value.append(biggest_number)
    return sum(max_value)


def minimum_sum(arr: list):
    min_value = []
    current_min_array = arr.copy()
    while len(current_min_array) > 1:
        smallest_number = min(current_min_array)
        current_min_array.remove(smallest_number)
        min_value.append(smallest_number)
    return sum(min_value)


def mini_max_sum(arr):
    max_sum = maximum_sum(arr)
    min_sum = minimum_sum(arr)

    return print(f"{min_sum} {max_sum}")


array = list(map(int, input().split()))
mini_max_sum(array)
