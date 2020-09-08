string = input()

list_1 = string.split()
list_2 = []

for element in list_1:
    element = -(int(element))
    list_2.append(element)

print(list_2)