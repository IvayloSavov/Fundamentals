import re

n = int(input())
pattern = r"^([!-z]+)>(\d{3})\|([a-z]{3})\|([A-Z]{3})\|([^<>]{3})<\1$"
# pattern = r"^([.+]+)>(\d{3})\|([a-z]{3})\|([A-Z]{3})\|([^<>]{3})<(\1)$"

for _ in range(n):
    password = input()
    valid_password = re.findall(pattern, password)

    if len(valid_password) == 0:
        print("Try another password!")
    else:
        for v_password in valid_password:
            print(f"Password: {v_password[1] + v_password[2] + v_password[3] + v_password[4]}")