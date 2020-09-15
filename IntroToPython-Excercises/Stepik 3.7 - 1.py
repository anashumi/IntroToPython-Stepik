input_lst = [str(input()) for i in range(int(input()))]
# print(input_lst)
# проверка инпута

lst = [i.split(";") for i in input_lst]
# print(lst)
# проверка правильности конверта

for elem in lst:
    elem[1] = int(elem[1])
    elem[3] = int(elem[3])
# print(lst)
# проверка правильности пределки в номер

players = []
for elem in lst:
    if elem[0] not in players:
        players.append(elem[0])
    if elem[2] not in players:
        players.append(elem[2])
# print(players)
# проверка правильности создяния списка

players_total_games = {}
players_wins = {}
players_ties = {}
players_losses = {}
players_points = {}

for elem in players:
    players_total_games = dict.fromkeys(players, 0)
    players_wins = dict.fromkeys(players, 0)
    players_ties = dict.fromkeys(players, 0)
    players_losses = dict.fromkeys(players, 0)
    players_points = dict.fromkeys(players, 0)
# print(players_total_games)
# проверка правильности записи в словари

for elem in lst:
    players_total_games[elem[0]] = players_total_games[elem[0]] + 1
    players_total_games[elem[2]] = players_total_games[elem[2]] + 1
    if elem[1] > elem[3]:
        players_wins[elem[0]] = players_wins[elem[0]] + 1
        players_points[elem[0]] = players_points[elem[0]] + 3
        players_losses[elem[2]] = players_losses[elem[2]] + 1
    elif elem[1] < elem[3]:
        players_wins[elem[2]] = players_wins[elem[2]] + 1
        players_points[elem[2]] = players_points[elem[2]] + 3
        players_losses[elem[0]] = players_losses[elem[0]] + 1
    elif elem[1] == elem[3]:
        players_ties[elem[0]] = players_ties[elem[0]] + 1
        players_points[elem[0]] = players_points[elem[0]] + 1
        players_ties[elem[2]] = players_ties[elem[2]] + 1
        players_points[elem[2]] = players_points[elem[2]] + 1

for elem in players:
    print(elem + ": " + str(players_total_games[elem])
          + " " + str(players_wins[elem]) + " " + str(players_ties[elem])
          + " " + str(players_losses[elem]) + " " + str(players_points[elem]))