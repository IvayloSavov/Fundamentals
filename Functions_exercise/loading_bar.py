integer = int(input())//10


def percent(number):
    symbol_percents = "%" * number
    return symbol_percents


def points(number):
    number_points = 10 - number
    symbol_points = "." * number_points
    return symbol_points


def loading_bar(number):
    if number == 10:
        print(f"{number*10}% Complete!")
        print(f"[{percent(integer)}]")
    else:
        print(f"{number*10}%", end=" ")
        print(f"[{percent(integer)}{points(integer)}]")
        print("Still loading...")


loading_bar(integer)