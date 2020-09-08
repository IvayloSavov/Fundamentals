import re

pattern = r"\|([A-Z]{4,})\|:#([A-Za-z]+ [A-Za-z]+)#"
n = int(input())

for _ in range(n):
    boss = input()
    valid_boss = re.findall(pattern, boss)

    if len(valid_boss) > 0:
        boss_name = valid_boss[0][0]
        title = valid_boss[0][1]
        print(f"{boss_name}, The {title}")
        print(f">> Strength: {len(boss_name)}")
        print(f">> Armour: {len(title)}")
    else:
        print("Access denied!")
