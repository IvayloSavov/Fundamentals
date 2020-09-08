from sys import maxsize
factor = int(input())
count = int(input())
elements_in_list = 0

my_list = []

for number in range(factor, count * factor + 1, factor):
    my_list.append(number)

print(my_list)