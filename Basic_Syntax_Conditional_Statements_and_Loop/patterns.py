highest_star = int(input())
current_star = 0
# Ascending
while current_star < highest_star:
    current_star += 1
    for star in range(1, current_star + 1):
        print("*", end= "")
    print()
# Desending

while highest_star > 1:
    highest_star -= 1
    for star_2 in range(1, highest_star + 1):
        print("*", end="")
    print()