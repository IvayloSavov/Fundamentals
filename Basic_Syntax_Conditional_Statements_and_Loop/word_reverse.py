s = input()
s_len = len(s)
reversed_s = ""

for index in range(len(s) - 1, -1, -1):
    reversed_s += s[index]

print(reversed_s)