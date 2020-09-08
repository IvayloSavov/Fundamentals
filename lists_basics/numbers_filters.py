n = int(input())

l = []
filtered_l = []

for _ in range(n):
    number = int(input())
    l.append(number)

command = input()

if command == "even":
    for element in l:
        if element % 2 == 0:
            filtered_l.append(element)
elif command == "odd":
    while len(l) > 0:
        e = l.pop(0)
        if e % 2 == 1:
            filtered_l.append(e)
elif command == "negative":
    for element in l:
        if element < 0:
            filtered_l.append(element)
elif command == "positive":
    while len(l) > 0:
        e = l.pop(0)
        if e >= 0:
            filtered_l.append(e)

print(filtered_l)