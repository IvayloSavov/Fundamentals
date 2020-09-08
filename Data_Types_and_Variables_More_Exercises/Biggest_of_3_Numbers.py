numbers = []

for _ in range(3):
    number = int(input())
    numbers.append(number)

print(max(numbers))

# Second way

# from sys import maxsize
#
# biggest_number = -maxsize
#
# for _ in range(3):
#     number = int(input())
#
#     if number > biggest_number:
#         biggest_number = number
#
# print(biggest_number)