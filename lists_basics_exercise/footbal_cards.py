PLAYERS_IN_TEAMS = 11

card = input()
list_card = card.split()

players_team_A = PLAYERS_IN_TEAMS
players_team_B = PLAYERS_IN_TEAMS
is_terminated = False

eliminated_players = []

for player in list_card:
    if "A" in player and player not in eliminated_players:
        eliminated_players.append(player)
        players_team_A -= 1

    elif "B" in player and player not in eliminated_players:
        eliminated_players.append(player)
        players_team_B -= 1

    if players_team_A < 7 or players_team_B < 7:
        is_terminated = True
        break #без break в judge взима 100/100

print(f"Team A - {players_team_A}; Team B - {players_team_B}")
if is_terminated:
    print("Game was terminated")
