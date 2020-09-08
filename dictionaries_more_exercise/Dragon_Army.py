from collections import defaultdict


def average_stats(not_average_stat, count_type_dragon):
    return f"{not_average_stat / count_type_dragon:.2f}"


n = int(input())

dragons_types_stats = defaultdict(dict)
count_dragons_by_type = defaultdict(int)
individual_stats = defaultdict(dict)

for _ in range(n):
    tokens = input().split()

    type_dragon, name, damage, health, armor = tokens[0], tokens[1], tokens[2], tokens[3], tokens[4]
    if damage == "null":
        damage = "45"
    if health == "null":
        health = "250"
    if armor == "null":
        armor = "10"
    damage, armor, health = int(damage), int(armor), int(health)
    key = type_dragon, name
    count_dragons_by_type[type_dragon] += 1
    if count_dragons_by_type[type_dragon] == 1:
        dragons_types_stats[type_dragon]["damage"] = 0
        dragons_types_stats[type_dragon]["armor"] = 0
        dragons_types_stats[type_dragon]["health"] = 0

    dragons_types_stats[type_dragon]["damage"] += damage
    dragons_types_stats[type_dragon]["armor"] += armor
    dragons_types_stats[type_dragon]["health"] += health

    individual_stats[key]["name"] = name
    individual_stats[key]["damage"] = damage
    individual_stats[key]["armor"] = armor
    individual_stats[key]["health"] = health

print()
individual_stats = dict(sorted(individual_stats.items(), key=lambda key_and_dict: key_and_dict[0][1]))

for type_dragon, values in dragons_types_stats.items():
    count_dragons = int(count_dragons_by_type[type_dragon])
    damage, health, armor = int(values["damage"]), int(values["health"]), int(values["armor"])
    average_damage = (average_stats(damage, count_dragons))
    average_health = (average_stats(health, count_dragons))
    average_armor = (average_stats(armor, count_dragons))
    print(f"{type_dragon}::({average_damage}/{average_health}/{average_armor})")
    for type_dragon_and_name, stats in individual_stats.items():
        if type_dragon in type_dragon_and_name[0]:
            name = type_dragon_and_name[1]
            damage, health, armor = int(stats["damage"]), int(stats["health"]), int(stats["armor"])
            print(f"-{name} -> damage: {damage}, health: {health}, armor: {armor}")
