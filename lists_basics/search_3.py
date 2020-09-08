n = int(input())
word = input()

l = []
filter_l = []

for _ in range(n):
    string = input()
    l.append(string)
    if word in string:
        filter_l.append(string)

print(l)
print(filter_l)