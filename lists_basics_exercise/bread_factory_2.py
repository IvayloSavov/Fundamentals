energy = 100
coins = 100
is_bankrupt = False
events = input().split("|")

for current_event in events:
    current_event_l = current_event.split("-")

    event = current_event_l[0]
    value = int(current_event_l[1])

    if event == "rest":
        gained_energy = 0
        if energy + value < 100:
            gained_energy = value
            energy += value
        else:
            gained_energy = 100 - energy
            energy = 100
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")

    elif event == "order":
        if energy < 30:
            energy += 50
            print("You had to rest!")
            continue
        else:
            energy -= 30
            coins += value
            print(f"You earned {value} coins.")

    else:
        ingredient = event
        if coins <= value:
            print(f"Closed! Cannot afford {ingredient}.")
            is_bankrupt = True
            break

        else:
            print(f"You bought {ingredient}.")
            coins -= value

if not is_bankrupt:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
