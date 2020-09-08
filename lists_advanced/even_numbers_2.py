numbers = map(int, input().split(", "))
print([index for index, number in enumerate(numbers) if number % 2 == 0])

# Горното, но на един ред
# print([index for index, number in enumerate(map(int, input().split(", "))) if number % 2 == 0])

