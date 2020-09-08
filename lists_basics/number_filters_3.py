n = int(input())

l = []
filtered_l = []

for _ in range(n):
    number = int(input())
    l.append(number)

command = input()

for number in l:
    filtered_passes = (
        (command == "even" and number % 2 == 0) or
        (command == "odd" and number % 2 == 1) or
        (command == "negative" and number < 0) or
        (command == "positive" and number >= 0)
    )
    if filtered_passes:
        filtered_l.append(number)

print(filtered_l)