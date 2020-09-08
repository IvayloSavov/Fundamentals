from sys import maxsize


def exchange(numbers):
    temp_numbers = numbers[index + 1:]
    temp_numbers += numbers[:index + 1]

    return temp_numbers


def get_index_max_even_sum(numbers):
    max_num = -maxsize
    index = -1  # слагаме тази стойност, за да видим дали после е влязло в цикъла, ако е влязло значи ще му е сменило и
    # стойността

    for i in range(len(numbers)):
        num = numbers[i]

        if num % 2 == 0 and num >= max_num:
            max_num = num
            index = i

    return index


def get_index_max_odd_sum(numbers):
    max_num = -maxsize
    index = -1  # слагаме тази стойност, за да видим дали после е влязло в цикъла, ако е влязло значи ще му е сменило и
    # стойността

    for i in range(len(numbers)):
        num = numbers[i]

        if num % 2 != 0 and num >= max_num:
            max_num = num
            index = i

    return index


def get_index_min_even_sum(numbers):
    min_num = maxsize
    index = -1  # слагаме тази стойност, за да видим дали после е влязло в цикъла, ако е влязло значи ще му е сменило и
    # стойността

    for i in range(len(numbers)):
        num = numbers[i]

        if num % 2 == 0 and num <= min_num:
            min_num = num
            index = i

    return index


def get_index_min_odd_sum(numbers):
    min_num = maxsize
    index = -1  # слагаме тази стойност, за да видим дали после е влязло в цикъла, ако е влязло значи ще му е сменило и
    # стойността

    for i in range(len(numbers)):
        num = numbers[i]

        if num % 2 != 0 and num <= min_num:
            min_num = num
            index = i

    return index


def get_count_first_even(numbers, count):
    temp_list = []
    counter = 0
    for num in numbers:
        if counter == count:
            break

        if num % 2 == 0:
            temp_list.append(num)
            counter += 1

    return temp_list


def get_count_first_odd(numbers, count):
    temp_list = []
    counter = 0
    for num in numbers:
        if counter == count:
            break

        if num % 2 != 0:
            temp_list.append(num)
            counter += 1

    return temp_list


def get_count_last_even(numbers, count):
    temp_list = []
    counter = 0
    for i in range(len(numbers) - 1, -1, -1):
        num = numbers[i]

        if counter == count:
            break

        if num % 2 == 0:
            temp_list.append(num)
            counter += 1

    temp_list.reverse()
    return temp_list


def get_count_last_odd(numbers, count):
    temp_list = []
    counter = 0
    for i in range(len(numbers) - 1, -1, -1):
        num = numbers[i]

        if counter == count:
            break

        if num % 2 != 0:
            temp_list.append(num)
            counter += 1

    temp_list.reverse()
    return temp_list


items = input().split()
numbers = []

for item in items:
    numbers.append(int(item))

command_input = input()

while command_input != "end":
    tokens = command_input.split()
    type_command = tokens[0]

    if type_command == "exchange":
        index = int(tokens[1])
        numbers = exchange(index)

        if index < 0 or index >= len(numbers):
            print("Invalid index")
            command_input = input()
            continue

    elif type_command == "max":
        criteria = tokens[1]
        index = -1
        if criteria == "even":
            index = get_index_max_even_sum(numbers)
        elif criteria == "odd":
            index = get_index_max_odd_sum(numbers)

        if index != -1:
            print(index)
        else:
            print("No matches")

    elif type_command == "min":
        criteria = tokens[1]
        index = -1

        if criteria == "even":
            index = get_index_min_even_sum(numbers)
        elif criteria == "odd":
            index = get_index_min_odd_sum(numbers)

        if index != -1:
            print(index)
        else:
            print("No matches")

    elif type_command == "first":
        count = int(tokens[1])

        if count > len(numbers):
            print("Invalid count")
            command_input = input()
            continue

        criteria = tokens [2]
        res = []
        if criteria == "even":
            res = get_count_first_even((numbers, count))
        elif criteria == "odd":
            res = get_count_first_odd(numbers, count)

        print(res)

    elif type_command == "last":
        count = int(tokens[1])

        if count > len(numbers):
            print("Invalid count")
            command_input = input()
            continue

        criteria = tokens[2]
        res = []

        if criteria == "even":
            res = get_count_last_even((numbers, count))
        elif criteria == "odd":
            res = get_count_last_odd(numbers, count)

        print(res)

    command_input = input()

print(numbers)