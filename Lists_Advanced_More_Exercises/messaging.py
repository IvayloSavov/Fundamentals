numbers = input().split()
string = list(input())
indexes = []

for number in numbers:
    index = []
    for digit in number:
        index.append(int(digit))
    indexes.append(sum(index))

message = ""

for i in indexes:
    if i > len(string) - 1:
        i = i % len(string)  # винаги като ти е казано от началото делиш на цялата дължина защото 28 % 28 си е 28
    message += string[i]
    string.pop(i)

print(message)