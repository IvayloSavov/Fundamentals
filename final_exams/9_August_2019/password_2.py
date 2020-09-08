import re

pattern = r"^(.+)>(\d{3})\|([a-z]{3})\|([A-Z]{3})\|([^<>]{3})<(\1)$"
n = int(input())

for i in range(n):
    password = input()

    match = re.fullmatch(pattern, password) # с fullmatch няма нужда от ^ и $ в началото и съответно края

    if match is None:
        print("Try another password!")
        continue

    group_one = match[2]
    group_two = match.group(3)
    group_three = match[4]
    group_four = match.group(5)

    encrypted_password = group_one + group_two + group_three + group_four

    print(f"Password: {encrypted_password}")