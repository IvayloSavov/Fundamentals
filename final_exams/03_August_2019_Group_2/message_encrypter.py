import re
pattern = r"(\*|@)([A-Z][a-z]{2,})\1: \[([A-Za-z])\]\|\[([A-Za-z])\]\|\[([A-Za-z])\]\|$"
n = int(input())

for _ in range(n):
    message = input()
    valid_message = re.findall(pattern, message)

    if len(valid_message) == 0:
        print("Valid message not found!")
    else:
        print(f"{valid_message[0][1]}: {ord(valid_message[0][2])} {ord(valid_message[0][3])} {ord(valid_message[0][4])}")
