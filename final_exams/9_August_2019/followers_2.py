likes = {}
comments = {}

while True:
    tokens = input()
    if tokens == "Log out":
        break
    tokens = tokens.split(": ")
    command = tokens[0]
    username = tokens[1]

    if command == "New follower":
        if username in likes:
            continue

        likes[username] = 0
        comments[username] = 0

    elif command == "Like":
        count = int(tokens[2])
        if username not in likes:
            likes[username] = 0
            comments[username] = 0

        likes[username] += count

    elif command == "Comment":
        if username not in comments:
            likes[username] = 0
            comments[username] = 0

        comments[username] += 1

    elif command == "Blocked":
        if username not in comments.keys():
            print(f"{username} doesn't exist.")
            continue
        comments.pop(username)
        likes.pop(username)

print(f"{len(likes.keys())} followers")

sorted_likes = dict(sorted(likes.items(), key=lambda u: (-u[1], u[0])))

for user, likes in sorted_likes.items():
    count_comments = comments[user]
    print(f"{user}: {likes + count_comments}")