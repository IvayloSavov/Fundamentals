text = input()
index_capital_letters = []

for index, character in enumerate(text):
    if character.isupper():
        index_capital_letters.append(index)

print(index_capital_letters)