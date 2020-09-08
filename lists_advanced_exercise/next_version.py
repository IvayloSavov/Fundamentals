current_version = input().split(".")

new_version = str(int("".join(current_version)) + 1)
# new_version_l = [element for element in new_version]
# print(".".join(new_version_l))
print(".".join(new_version))

# print(".".join(str(int("".join(input().split("."))) + 1)))