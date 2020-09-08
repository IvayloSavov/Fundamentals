needed_experience = float(input())
battles = int(input())

count_battles = 0
total_experience = 0

for battle in range(1, battles + 1):
    count_battles += 1
    gained_experience = float(input())

    if battle % 5 == 0:
        fifth_game_experience = gained_experience * 90/100
        total_experience += fifth_game_experience
    if battle % 3 == 0:
        third_game_experience = gained_experience * 115/100
        total_experience += third_game_experience
    elif not battle % 5 == 0 and not battle % 3 == 0:
        total_experience += gained_experience

    if total_experience >= needed_experience:
        break

if total_experience >= needed_experience:
    print(f"Player successfully collected his needed experience for {count_battles} battles.")
else:
    print(f"Player was not able to collect the needed experience, {needed_experience - total_experience:.2f} more needed.")

