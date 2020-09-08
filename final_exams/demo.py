l = input()

l_sum = sum(list(map(lambda x: ord(x), l)))
print(l_sum)

l_sum = sum([ord(ch) for ch in l])
print(l_sum)