def sum_numbers(a, b):
    res = a + b
    return res


def subtract(a, b):
    return a - b


def sum_and_subtract(a, b, c):
    sum = sum_numbers(a, b)
    res = subtract(sum, c)
    return res

a = int(input())
b = int(input())
c = int(input())

print(sum_and_subtract(a, b, c))

