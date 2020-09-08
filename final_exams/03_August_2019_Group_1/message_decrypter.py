import re

n = int(input())
pattern = r"^(\$|\%)([A-Z][a-z]{2,})\1: \[([0-9]+)\]\|\[([0-9]+)\]\|\[([0-9]+)\]\|$"

for _ in range(n):
    message = input()
    valid_messages = re.findall(pattern, message)

    if len(valid_messages) == 0:
        print("Valid message not found!")
    else:
        for valid_message in valid_messages:
            text = chr(int(valid_message[2])) + chr(int(valid_message[3])) + chr(int(valid_message[4]))
            print(f"{valid_message[1]}: {text}")