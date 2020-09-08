from math import ceil
numbers = list(map(int, input().split(", ")))

max_num = max(numbers)
number_of_groups = ceil(max_num / 10)

for group in range(1, number_of_groups + 1):
    upper_border = group * 10
    lower_border = upper_border - 10
    current_group = [number for number in numbers if lower_border < number <= upper_border]
    # for element in current_group: може и да ги махаме, за да не ги проверява, но не е необходимо
    #     numbers.remove(element)
    print(f"Group of {group * 10}'s: {current_group}")
