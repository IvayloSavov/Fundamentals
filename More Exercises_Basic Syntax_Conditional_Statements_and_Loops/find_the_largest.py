from sys import maxsize
number = input()
numbers = []
biggest_numbers = []

for digit in number:
    numbers.append(int(digit))

while len(numbers) > 0:
    max_number = -maxsize
    for current_number in numbers:
        if current_number > max_number:
            max_number = current_number
    numbers.remove(max_number)
    biggest_numbers.append(max_number)


while len(biggest_numbers) > 0:
    print(biggest_numbers.pop(0), end="")
