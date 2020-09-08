strings = input().split(" ")

print("".join([string * len(string) for string in strings]))