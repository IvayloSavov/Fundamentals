def factorial_first(number):
    factorial = 1
    for multiplier in range(number, 0, -1):
        factorial = factorial * multiplier
    return factorial


def factorial_second(number):
    factorial = 1
    for multiplier in range(number, 0, -1):
        factorial = factorial * multiplier
    return factorial


def factorial_division():
    result = factorial_first(integer_1) / factorial_second(integer_2)
    return f"{result:.2f}"


integer_1 = int(input())
integer_2 = int(input())
print(factorial_division())