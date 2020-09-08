from math import factorial


def factorial_first(number):
    fact = factorial(number)
    return fact


def factorial_second(number):
    fact = factorial(number)
    return fact


def factorial_division():
    result = factorial_first(integer_1) / factorial_second(integer_2)
    return f"{result:.2f}"


integer_1 = int(input())
integer_2 = int(input())
print(factorial_division())