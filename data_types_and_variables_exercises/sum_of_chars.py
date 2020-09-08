number_lines = int(input())
sum_equals = 0

for character in range(number_lines):
    letter = input()
    sum_equals += ord(letter)

print(f"The sum equals: {sum_equals}")