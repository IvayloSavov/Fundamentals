def is_posititve(number):
    if number > 0:
        return True


def sum_divisors(number):
    divisors = 0
    for divisor in range(1, number):
        if number % divisor == 0:
            divisors += divisor
    return divisors


def perfect_number(number):
    if is_posititve(number) and sum_divisors(number) == number:
        return 'We have a perfect number!'
    else:
        return "It's not so perfect."


number = int(input())
print(perfect_number(number))