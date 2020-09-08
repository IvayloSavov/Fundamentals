users = {}
max_capacity = int(input())

while True:
    token = input()
    if token == "Statistics":
        break
    token = token.split("=")
    command = token[0]

    if command == "Add":
        username = token[1]
        sent = int(token[2])
        received = int(token[3])

        if username in users:
            continue
        else:
            users[username] = [sent, received]

    elif command == "Message":
        sender = token[1]
        receiver = token[2]

        if sender in users.keys() and receiver in users.keys():
            users[sender][0] += 1
            users[receiver][1] += 1

            if sum(users[sender]) >= max_capacity:
                print(f"{sender} reached the capacity!")
                users.pop(sender)

            if sum(users[receiver]) >= max_capacity:
                print(f"{receiver} reached the capacity!")
                users.pop(receiver)

    elif command == "Empty":
        username = token[1]

        if username == "All":
            users.clear()

        elif username in users:
            users.pop(username)

print(f"Users count: {len(users.keys())}")

users = dict(sorted(users.items(), key=lambda user: (-int(user[1][1]), user[0])))

for user, send_received in users.items():
    print(f"{user} - {sum(send_received)}")

