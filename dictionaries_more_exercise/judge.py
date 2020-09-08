from collections import defaultdict

all_contest = []
all_users_in_contest = defaultdict(dict)
individual_statistics = defaultdict(int)

while True:
    tokens = input()
    if tokens == "no more time":
        break
    tokens = tokens.split(" -> ")
    username, contest, points = tokens[0], tokens[1], int(tokens[2])

    if contest in all_contest:
        if username in all_users_in_contest[contest].keys():
            if all_users_in_contest[contest][username] < points:
                current_points = all_users_in_contest[contest][username]
                all_users_in_contest[contest][username] = points
                individual_statistics[username] -= current_points
                individual_statistics[username] += points
        else:
            all_users_in_contest[contest][username] = points
            individual_statistics[username] += points
    else:
        all_contest.append(contest)
        all_users_in_contest[contest][username] = points
        individual_statistics[username] += points

for contest in all_contest:
    users_position_in_contest = 1
    print(f"{contest}: {len(all_users_in_contest[contest].keys())} participants")
    current_contest_participants = all_users_in_contest[contest]
    sorted_current_contest_participants = dict(sorted(current_contest_participants.items(),
                                                      key=lambda participant_and_points: (
                                                      -participant_and_points[1], participant_and_points[0])))
    for user, points in sorted_current_contest_participants.items():
        print(f"{users_position_in_contest}. {user} <::> {points}")
        users_position_in_contest += 1


print("Individual standings:")
sorted_individual_statistics = dict(sorted(individual_statistics.items(), key=lambda user_and_points: (-user_and_points[
    1], user_and_points[0])))
users_position = 1

for username, points in sorted_individual_statistics.items():
    print(f"{users_position}. {username} -> {points}")
    users_position += 1
