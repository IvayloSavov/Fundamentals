string = input()
encrypted_text = ""

for ch in string:
    ch_to_encrypt = chr(ord(ch) + 3)
    encrypted_text += ch_to_encrypt

print(encrypted_text)