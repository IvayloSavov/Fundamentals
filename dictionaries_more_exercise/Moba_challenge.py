from collections import defaultdict

players_pool = defaultdict(dict)

while True:
    tokens = input()
    if tokens == "Season end":
        break

    if "vs" in tokens:
        player_1, player_2 = tokens.split(" vs ")
        if player_1 in players_pool.keys() and player_2 in players_pool.keys():
            player_1_positions = players_pool[player_1].keys()
            player_2_positions = players_pool[player_2].keys()
            same_positions_players_skill_points = defaultdict(list)

            for position in player_1_positions:
                if position in player_2_positions:
                    player_1_points = players_pool[player_1][position]
                    player_2_points = players_pool[player_2][position]
                    same_positions_players_skill_points[player_1].append(player_1_points)
                    same_positions_players_skill_points[player_2].append(player_2_points)

            if sum(same_positions_players_skill_points[player_1]) > \
                    sum(same_positions_players_skill_points[player_2]):
                players_pool.pop(player_2)

            elif sum(same_positions_players_skill_points[player_2]) > \
                    sum(same_positions_players_skill_points[player_1]):
                players_pool.pop(player_1)

            #######################################################################

    else:
        tokens = tokens.split(" -> ")
        player, position, skill = tokens[0], tokens[1], int(tokens[2])

        if player in players_pool.keys():
            player_positions = players_pool[player].keys()
            if position in player_positions:
                current_skill = players_pool[player][position]
                if current_skill < skill:
                    players_pool[player][position] = skill
            else:
                players_pool[player][position] = skill

        else:
            players_pool[player][position] = skill

all_players_total_skill = defaultdict(int)

for player in players_pool.keys():
    player_total_skill_points = [int(skill_points) for skill_points in players_pool[player].values()]
    all_players_total_skill[player] += sum(player_total_skill_points)

sorted_players = dict(sorted(all_players_total_skill.items(),
                             key=lambda player_and_skill_point:
                             (-player_and_skill_point[1], player_and_skill_point[0])))

for player, skill_points in sorted_players.items():
    print(f"{player}: {skill_points} skill")
    current_player_positions_and_skill_points = players_pool[player]
    sorted_current_player_positions_and_skill_points = dict(sorted(current_player_positions_and_skill_points.items(),
                                                                   key=lambda position_and_skill: (
                                                                       -position_and_skill[1],
                                                                       position_and_skill[0])))

    for position, skill in sorted_current_player_positions_and_skill_points.items():
        print(f"- {position} <::> {skill}")
