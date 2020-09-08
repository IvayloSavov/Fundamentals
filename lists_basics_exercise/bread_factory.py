energy = 100
coins = 100
is_bankrupt = False
events = input().split("|")

for current_event in events:
    current_event_l = current_event.split("-")

    event = current_event_l[0]
    value = int(current_event_l[1])

    if event == "rest":
        if energy >= 100:
            print("You gained 0 energy.")
        else:
            energy += value
            print(f"You gained {value} energy.")
        if energy > 100:
            energy = 100
        print(f"Current energy: {energy}.")

    elif event == "order":
        if energy >= 30:
            energy -= 30
            coins += value
            print(f"You earned {value} coins.")
        else:
            energy += 50
            print("You had to rest!")
            continue

    else:
        ingredient = event
        if coins > value:
            print(f"You bought {ingredient}.")
            coins -= value
        else:
            print(f"Closed! Cannot afford {ingredient}.")
            is_bankrupt = True
            break

if not is_bankrupt:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
