string_1 = input().split(", ")
string_2 = input().split(", ")

substrings = []

for fr_str in string_1:
    for scn_str in string_2:
        if fr_str in scn_str:
            substrings.append(fr_str)
            break

print(substrings)

