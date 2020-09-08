animals = input().split(", ")

# animals = animals[::-1]
sheep_counter = 0
for i in range(len(animals) - 1, -1, -1):
    if animals[len(animals) - 1] == "wolf":
        print("Please go away and stop eating my sheep")
        break
    else:
        current_animal = animals[i]
        if current_animal == "sheep":
            sheep_counter += 1
        elif current_animal == "wolf":
            print(f"Oi! Sheep number {sheep_counter}! You are about to be eaten by a wolf!")
            break

