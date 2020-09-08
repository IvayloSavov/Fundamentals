n = int(input())
word = input()

l = []
filter_l = []

for _ in range(n):
    string = input()
    l.append(string)

print(l)

for element in l:
    if word in element:
        filter_l.append(element)

print(filter_l)