list_num_str = input().split(", ")
amount_of_beggars = int(input())

# 1. From list_num_str to list_num_int
list_num_int = []

while len(list_num_str) > 0:
    element = list_num_str.pop(0)
    list_num_int.append(int(element))

# 2. Create the beggars list with their positions to sum what they have collected
l_beggars = []

for beggar in range(amount_of_beggars):
    l_beggars.append(0)

# 3. Seperate the list to every beggar

beggar_index = 0

for e in list_num_int:
    l_beggars[beggar_index] += e
    beggar_index += 1

    if beggar_index == amount_of_beggars:
        beggar_index = 0

print(l_beggars)