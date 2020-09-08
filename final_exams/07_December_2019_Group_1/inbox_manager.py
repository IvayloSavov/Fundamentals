users = {}

while True:
    tokens = input()
    if tokens == "Statistics":
        break
    tokens = tokens.split("->")
    command = tokens[0]
    username = tokens[1]

    if command == "Add":
        if username in users.keys():
            print(f"{username} is already registered")
        else:
            users[username] = []

    elif command == "Send":
        email = tokens[2]
        if username in users.keys():
            users[username].append(email)

    elif command == "Delete":
        if username in users.keys():
            users.pop(username)
        else:
            print(f"{username} not found!")

users = dict(sorted(users.items(), key=lambda user: (-len(user[1]), user[0])))

print(f"Users count: {len(users.keys())}")

for user, emails in users.items():
    print(user)
    for email in emails:
        print(f" - {email}")