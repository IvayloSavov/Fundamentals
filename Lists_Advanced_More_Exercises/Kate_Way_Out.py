rows = int(input())
maze = []

for _ in range(rows):
    maze_row = input()
    maze.append(maze_row) # с extend ще вкара всеки един символ поотделно, защото не е списък

rows = len(maze)
moves = 1
no_exit = False

for index, row in enumerate(maze):
    if "k" in row:
        k_index = row.index("k")

        if maze[index][k_index - 1] == " ":
            moves += 1
        elif maze[index][k_index + 1] == " ":
            moves += 1
        else:
            print("Kate cannot get out")
            break

        while rows > 0:
            pass

    rows -= 1
