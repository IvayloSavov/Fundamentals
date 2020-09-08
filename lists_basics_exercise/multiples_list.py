from sys import maxsize
factor = int(input())
count = int(input())
elements_in_list = 0

my_list = []

for number in range (1, maxsize):
    if number % factor == 0:
        my_list.append(number)
        elements_in_list += 1
    if elements_in_list == count:
        break

print(my_list)