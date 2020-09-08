string = input()

digits = [] # или с листове или със стрингове
letters = []
other_characters = []

for ch in string:
    if ch.isdigit():
        digits.append(ch)
    elif ch.isalpha():
        letters.append(ch)
    else:
        other_characters.append(ch)

print("".join(digits))
print("".join(letters))
print("".join(other_characters))
