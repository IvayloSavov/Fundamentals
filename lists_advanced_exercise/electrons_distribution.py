total_electrons = int(input())
shells = []
index = 0

while total_electrons > 0:
    current_shell_electrons = 2*((index + 1) ** 2)
    if total_electrons >= current_shell_electrons:
        shells.insert(index, current_shell_electrons)
    else:
        shells.insert(index, total_electrons)
        break
    index += 1
    total_electrons -= current_shell_electrons

print(shells)
