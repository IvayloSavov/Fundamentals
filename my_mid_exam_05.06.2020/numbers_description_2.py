numbers = list(map(int, input().split()))
numbers_sum = sum(numbers)
count_numbers = len(numbers)

average_value = numbers_sum/count_numbers
greater_than_the_average = [element for element in numbers if element > average_value]

if len(greater_than_the_average) == 0:
    print("No")
else:
    count = 0
    first_5_greater = []
    while len(greater_than_the_average) > 0:
        max_num = max(greater_than_the_average)
        max_num_index = greater_than_the_average.index(max_num)
        first_5_greater.append(max_num)
        greater_than_the_average.pop(max_num_index)
        count += 1
        if count == 5:
            break
    first_5_greater = list(map(str, first_5_greater))
    print(" ".join(first_5_greater))
