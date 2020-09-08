numbers = list(map(int, input().split()))
numbers_sum = sum(numbers)
count_numbers = len(numbers)

average_value = numbers_sum/count_numbers
greater_than_the_average = []

for element in numbers:
    if element > average_value:
        greater_than_the_average.append(element)

if len(greater_than_the_average) == 0:
    print("No")
else:
    count = 0
    first_5_greater = []
    greater_than_the_average.sort(reverse=True)
    for number in greater_than_the_average:
        first_5_greater.append(number)
        count += 1
        if count == 5:
            break
    first_5_greater.sort(reverse=True)
    first_5_greater = list(map(str, first_5_greater))
    print(" ".join(first_5_greater))


