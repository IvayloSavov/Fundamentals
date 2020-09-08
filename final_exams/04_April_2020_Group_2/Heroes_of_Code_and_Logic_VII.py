MAX_HEALTH = 100
MAX_MANA_POINTS = 200

number_heroes = int(input())

heroes = {}

for hero in range(1, number_heroes + 1):
    hero_name, hp, mp = input().split()

    if hero_name not in heroes:
        heroes[hero_name] = []
        heroes[hero_name].append(int(hp))
        heroes[hero_name].append(int(mp))
    else:
        heroes[hero_name][0] += int(hp)
        heroes[hero_name][1] += int(mp)

        if heroes[hero_name][0] > MAX_HEALTH:
            heroes[hero_name][0] = MAX_HEALTH

        if heroes[hero_name][1] > MAX_MANA_POINTS:
            heroes[hero_name][1] = MAX_MANA_POINTS

while True:
    command_input = input()
    if command_input == "End":
        break
    tokens = command_input.split(" - ")

    if tokens[0] == "CastSpell":
        hero_name, mp_needed, spell_name = tokens[1], tokens[2], tokens[3]
        if heroes[hero_name][1] >= int(mp_needed):
            heroes[hero_name][1] -= int(mp_needed)
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name][1]} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif tokens[0] == "TakeDamage":
        hero_name, damage, attacker = tokens[1], tokens[2], tokens[3]
        heroes[hero_name][0] -= int(damage)

        if heroes[hero_name][0] <= 0:
            print(f"{hero_name} has been killed by {attacker}!")
            heroes.pop(hero_name)
            continue
        print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name][0]} HP left!")

    elif tokens[0] == "Recharge":
        hero_name, amount = tokens[1], tokens[2]
        old_mp = heroes[hero_name][1]
        new_mp = heroes[hero_name][1] + int(amount)

        if new_mp > MAX_MANA_POINTS:
            print(f"{hero_name} recharged for {MAX_MANA_POINTS - old_mp} MP!")
            heroes[hero_name][1] = MAX_MANA_POINTS
            continue

        print(f"{hero_name} recharged for {amount} MP!")
        heroes[hero_name][1] = new_mp

    elif tokens[0] == "Heal":
        hero_name, amount = tokens[1], tokens[2]
        old_hp = heroes[hero_name][0]
        new_hp = heroes[hero_name][0] + int(amount)

        if new_hp > MAX_HEALTH:
            print(f"{hero_name} healed for {MAX_HEALTH - old_hp} HP!")
            heroes[hero_name][0] = MAX_HEALTH
            continue

        print(f"{hero_name} healed for {amount} HP!")
        heroes[hero_name][0] = new_hp

# sorting heroes
heroes = dict(sorted(heroes.items(), key=lambda hero_s: (-hero_s[1][0], hero_s[0])))

for hero, hp_mp in heroes.items():
    print(f"{hero}")
    print(f"  HP: {hp_mp[0]}")
    print(f"  MP: {hp_mp[1]}")
