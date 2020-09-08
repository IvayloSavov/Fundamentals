n = int(input())

l = []
filtered_l = []

for _ in range(n):
    number = int(input())
    l.append(number)

command = input()

for number in l:
    if command == "even" and number % 2 == 0:
        filtered_l.append(number)
    elif command == "odd" and number % 2 == 1:
        filtered_l.append(number)
    elif command == "negative" and number < 0:
        filtered_l.append(number)
    elif command == "positive" and number >= 0:
        filtered_l.append(number)

print(filtered_l)