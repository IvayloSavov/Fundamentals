import re
text_to_decipher = input()
substrings = input().split(" ")
pattern = r"^[d-z\{\}\|\#]+$"

valid_text = re.findall(pattern, text_to_decipher)

if len(valid_text) > 0:
    # valid_text = [chr(ord(ch) - 3) for ch in valid_text[0]]
    valid_text = list(map(lambda ch: chr(ord(ch) - 3), valid_text[0]))
    valid_text = "".join(valid_text)
    valid_text = valid_text.replace(substrings[0], substrings[1])
    print(valid_text)
else:
    print("This is not the book you are looking for.")
