import re

pattern = r"(@#{1,})([A-Z][A-Za-z0-9]{4,}[A-Z])(@#{1,})"
n = int(input())
words = []

for _ in range(n):
    text = input()
    matches = re.findall(pattern, text)

    if len(matches) <= 0:
        print("Invalid barcode")
        continue

    for match in matches:
        word = match[1]
        digits = [ch for ch in word if ch.isdigit()]
        if len(digits) > 0:
            print(f"Product group: {''.join(digits)}")
        else:
            print(f"Product group: 00")