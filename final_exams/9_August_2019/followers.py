followers = {}

while True:
    tokens = input()
    if tokens == "Log out":
        break
    tokens = tokens.split(": ")
    command = tokens[0]
    username = tokens[1]

    if command == "New follower":
        if username not in followers.keys():
            followers[username] = [0, 0]

    elif command == "Like":
        count = int(tokens[2])
        if username not in followers.keys():
            followers[username] = [0, 0]

        followers[username][0] += count

    elif command == "Comment":
        if username not in followers.keys():
            followers[username] = [0, 0]

        followers[username][1] += 1

    elif command == "Blocked":
        if username not in followers.keys():
            print(f"{username} doesn't exist.")
            continue
        followers.pop(username)

followers = dict(sorted(followers.items(), key=lambda follower: (-follower[1][0], follower[0])))
print(f"{len(followers.keys())} followers")

for follower, likes_comment in followers.items():
    print(f"{follower}: {sum(likes_comment)}")

