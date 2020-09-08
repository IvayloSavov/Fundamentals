from collections import defaultdict

all_contest = {}
users_take_part_in = defaultdict(dict)

while True:
    tokens = input()
    if tokens == "end of contests":
        break
    tokens = tokens.split(":")
    contest = tokens[0]
    password = tokens[1]

    all_contest[contest] = password

while True:
    tokens = input()
    if tokens == "end of submissions":
        break
    tokens = tokens.split("=>")
    contest_1 = tokens[0]
    password = tokens[1]
    username = tokens[2]
    points = int(tokens[3])

    if contest_1 in all_contest.keys() and all_contest[contest_1] == password:
        if username in users_take_part_in.keys():
            if contest_1 in users_take_part_in[username].keys():
                if points > users_take_part_in[username][contest_1]:
                    users_take_part_in[username][contest_1] = points
            else:
                users_take_part_in[username][contest_1] = points
        else:
            users_take_part_in[username][contest_1] = points

max_points = 0
user_with_max_points = ""

for user in users_take_part_in.keys():
    points_user = sum(users_take_part_in[user].values())

    if points_user > max_points:
        max_points = points_user
        user_with_max_points = user

print(f"Best candidate is {user_with_max_points} with total {max_points} points.\n"
      "Ranking:")

sorted_users = sorted(users_take_part_in.keys(), key=lambda name: name)

for user in sorted_users:
    print(user)
    users_contests_and_points = dict(sorted(users_take_part_in[user].items(), key=lambda contest_and_points:
                                            contest_and_points[1], reverse=True))

    for contest, points in users_contests_and_points.items():
        print(f"#  {contest} -> {points}")
