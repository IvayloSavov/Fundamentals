from sys import maxsize
l_num_str = input().split()
numbers_to_remove = int(input())

# 1. list_str to list_num
l_num = []

for num_str in l_num_str:
    l_num.append(int(num_str))


# 2. Remove the smallest one

for remove in range(numbers_to_remove):
    smallest_number = maxsize # number time to remove a number
    for num in l_num: # check which one is the smallest
        if num < smallest_number:
            smallest_number = num
    l_num.remove(smallest_number)

print(l_num)
