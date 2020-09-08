import re
from functools import reduce
from math import prod


def multiply_list(my_list):
    result = 1
    for digit in my_list:
        result = result * digit
    return result


string = input()
pattern = r"(:{2}|\*{2})([A-Z]{1}[a-z]{2,})(\1)"

matches = re.findall(pattern, string)
cool_threshold_digits = list(map(int, re.findall(r"\d", string)))
result_threshold = reduce(lambda x, y: x * y, cool_threshold_digits)
# result_threshold = prod(cool_threshold_digits)
# result_threshold = multiply_list(cool_threshold_digits)

print(f"Cool threshold: {result_threshold}")
print(f"{len(matches)} emojis found in the text. The cool ones are:")

for match in matches:
    word = match[1]
    word_ascii = sum([ord(ch) for ch in word])
    if word_ascii >= result_threshold:
        print("".join(match))
