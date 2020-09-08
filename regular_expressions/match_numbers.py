import re

pattern = r"(((^|(?<=\s))(-*)(\d+)((\.\d+)*)($|(?=\s))))"

text = input()
matches = re.findall(pattern, text)

for math in matches:
    number, *others = math
    print(number, end=" ")