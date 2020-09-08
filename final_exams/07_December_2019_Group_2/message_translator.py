import re

pattern = r"!([A-Z][a-z]{2,})!:\[([A-Za-z]{8,})\]"
n = int(input())

for _ in range(n):
    text = input()
    valid_text = re.findall(pattern, text)

    if len(valid_text) > 0:
        ord_characters = list(map(lambda ch: str(ord(ch)), valid_text[0][1]))
        print(f"{valid_text[0][0]}: {' '.join(ord_characters)}")
    else:
        print("The message is invalid")
