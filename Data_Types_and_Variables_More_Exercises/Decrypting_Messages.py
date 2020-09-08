key = int(input())
n = int(input())

message = ""

for _ in range(n):
    character = input()
    new_chr = chr(ord(character) + key)
    message += new_chr

print(message)