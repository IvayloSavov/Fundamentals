n = int(input())
word = input()

l = []
filter_l = []

for _ in range(n):
    string = input()
    l.append(string)

print(l)

for i in range (len(l) - 1, -1, -1):
    element = l[i]
    if element not in l:
        l.pop(i)
