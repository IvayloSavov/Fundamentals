def staircase(size):
    builded_staircase = []
    spaces_on_each_row = size - 1
    for _ in range(size):
        current_row = (" " * spaces_on_each_row) + ("#" * (size - spaces_on_each_row))
        spaces_on_each_row -= 1
        builded_staircase.append(current_row)
    return "\n".join(builded_staircase)


size_of_staircase = int(input())
print(staircase(size_of_staircase))