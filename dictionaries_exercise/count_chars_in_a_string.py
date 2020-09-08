from _collections import defaultdict

string = input()
occurrences = defaultdict(int)

for character in string:
    if character == " ":
        continue
    occurrences[character] += 1

for character, count in occurrences.items():
    print(f"{character} -> {count}")
