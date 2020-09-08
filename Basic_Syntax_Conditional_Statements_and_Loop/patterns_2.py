GROW = 1
SHRINK = -1

desired_size = int(input())
direction = GROW
curent_size = 0

while (curent_size < desired_size and direction == GROW) or (direction == SHRINK and curent_size > 0):
    curent_size += direction
    print("*" * curent_size)

    if desired_size == curent_size:
        direction = SHRINK