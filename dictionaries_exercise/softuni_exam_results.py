from _collections import defaultdict

participants = defaultdict(int)
languages = defaultdict(int)

while True:
    command = input()
    if command == "exam finished":
        break

    command = command.split("-")

    username = command[0]
    language = command[1]

    if language == "banned" and username in participants.keys():
        participants.pop(username)
        continue

    points = int(command[2])

    languages[language] += 1

    if username in participants.keys():
        if points > participants[username]:
            participants[username] = points
    else:
        participants[username] += points

# Sorting the participants
participants = dict(sorted(participants.items(), key=lambda x: (-x[1], x[0])))

print("Results:")
for participant, points in participants.items():
    print(f"{participant} | {points}")


# Sorting the languages
languages = dict(sorted(languages.items(), key=lambda x: (-x[1], x[0])))
print('Submissions:')
for language, points in languages.items():
    print(f"{language} - {points}")













