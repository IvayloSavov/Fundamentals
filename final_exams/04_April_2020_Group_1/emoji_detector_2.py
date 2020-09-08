from functools import reduce
import re

string = input()
pattern = r"(:{2}|\*{2})([A-Z]{1}[a-z]{2,})(\1)" # ако двойката за : и * е само една, това означава, че има вариант,
# в който може да имаме и :*, а не трябва да има такъв случай.
matches = list(re.finditer(pattern, string))
digits = list(map(int, re.findall("\d", string)))
cool_threshold = reduce(lambda x, y: x * y, digits)

print(f"Cool threshold: {cool_threshold}")
print(f"{len(matches)} emojis found in the text. The cool ones are:")

for match in matches:
    emoji = match.group(0)
    word = match.group(2)
    ascii_sum_word = sum(list(map(lambda ch: ord(ch), word)))
    if ascii_sum_word >= cool_threshold:
        print(emoji)

