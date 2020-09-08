import re

pattern = r"(\d+)"
while True:
    text = input()

    if not text:
        break

    res = re.findall(pattern, text)

    for match in res:
        print(match, end=" ")