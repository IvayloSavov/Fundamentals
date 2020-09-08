from _collections import defaultdict

MAX_HP = 100
MAX_MP = 200

number_of_heroes = int(input())
heroes_hp = defaultdict(int)
heroes_mp = defaultdict(int)

for _ in range(1, number_of_heroes + 1):
    tokens = input().split()
    hero_name, hp, mp = tokens[0], int(tokens[1]), int(tokens[2])

    heroes_hp[hero_name] += hp
    heroes_mp[hero_name] += mp

    if heroes_hp[hero_name] > MAX_HP:
        heroes_hp[hero_name] = MAX_HP

    if heroes_mp[hero_name] > MAX_MP:
        heroes_mp[hero_name] = MAX_MP

while True:
    tokens = input()
    if tokens == "End":
        break
    tokens = tokens.split(" - ")
    command = tokens[0]
    hero_name = tokens[1]

    if command == "CastSpell":
        mp_needed = int(tokens[2])
        spell_name = tokens[3]
        if heroes_mp[hero_name] < mp_needed:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
        else:
            heroes_mp[hero_name] -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes_mp[hero_name]} MP!")

    elif command == "TakeDamage":
        damage = int(tokens[2])
        attacker = tokens[3]
        heroes_hp[hero_name] -= damage
        if heroes_hp[hero_name] <= 0:
            print(f"{hero_name} has been killed by {attacker}!")
            heroes_hp.pop(hero_name)
            heroes_mp.pop(hero_name)
        else:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes_hp[hero_name]} HP left!")

    elif command == "Recharge":
        amount = int(tokens[2])
        if heroes_mp[hero_name] + amount > MAX_MP:
            amount = MAX_MP - heroes_mp[hero_name]
            heroes_mp[hero_name] = MAX_MP
        else:
            heroes_mp[hero_name] += amount
        print(f"{hero_name} recharged for {amount} MP!")

    elif command == "Heal":
        amount = int(tokens[2])
        if heroes_hp[hero_name] + amount > MAX_HP:
            amount = MAX_HP - heroes_hp[hero_name]
            heroes_hp[hero_name] = MAX_HP
        else:
            heroes_hp[hero_name] += amount
        print(f"{hero_name} healed for {amount} HP!")

sorted_heroes = dict(sorted(heroes_hp.items(), key=lambda hero: (-hero[1], hero[0])))

for hero, hp in sorted_heroes.items():
    print(f"{hero}")
    print(f"  HP: {hp}")
    print(f"  MP: {heroes_mp[hero]}")