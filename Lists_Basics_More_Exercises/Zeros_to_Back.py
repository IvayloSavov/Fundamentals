string = list(map(int, input().split(", ")))

count_0 = string.count(0)

while 0 in string:
    string.remove(0)

while count_0 > 0:
    string.append(0)
    count_0 -= 1

print(string)