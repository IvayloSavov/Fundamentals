n = int(input())
word = input()

l = []
filter_l = []

for _ in range(n):
    string = input()
    l.append(string)

print(l)

l_len = len(l)
while len(l) > 0:
    e = l.pop(0)
    if word in e:
        filter_l.append(e)

print(filter_l)