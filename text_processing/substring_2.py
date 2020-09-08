replace_string = input()
actual_string = input()

while replace_string in actual_string:
    actual_string = actual_string.replace(replace_string, "")

print(actual_string)