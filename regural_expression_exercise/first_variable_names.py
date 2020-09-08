import re

# pattern = r"\b_([a-zA-Z0-9]+)\b"
pattern = r"\b_(?P<variable>[a-zA-Z0-9]+)\b" # с име

text = input()
matches = re.finditer(pattern, text)
result_matches = [] # може и с лист компрехенсион
for match in matches:
    result_matches.append(match.group(1))
    # print(f"{match.group('variable')}", end=", ")
    # print(match['variable'])
    # print(match[1])
    # print(match[0]) - връща целия мач, докато с единица връща само групата
    # print(match.group(0))
    # # print(match.group(1))- отново връща целия мач
print(",".join(result_matches))
