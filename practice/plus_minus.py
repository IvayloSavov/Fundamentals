def find_positive_numbers(arr):
    positive_numbers = [n for n in arr if n > 0]
    return len(positive_numbers)


def find_negative_numbers(arr):
    negative_numbers = list(filter(lambda n: n < 0, arr))
    return len(negative_numbers)


def ratios_plus_minus_zero(arr: list, count_all_numbers):
    count_positive_numbers = find_positive_numbers(arr)
    count_negative_numbers = find_negative_numbers(arr)
    count_0 = arr.count(0)

    ratio_positive = count_positive_numbers / count_all_numbers
    ratio_negative = count_negative_numbers / count_all_numbers
    ratio_zero = count_0 / count_all_numbers

    res = (
        f"{ratio_positive:.6f}\n"
        f"{ratio_negative:.6f}\n"
        f"{ratio_zero:.6f}"
    )

    return print(res)


count_numbers = int(input())
numbers = list(map(int, input().split()))

ratios_plus_minus_zero(numbers, count_numbers)
