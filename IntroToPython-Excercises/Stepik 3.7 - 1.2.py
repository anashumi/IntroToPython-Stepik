class TeamStats:
    team_games = 0
    team_wins = 0
    team_ties = 0
    team_losses = 0
    team_points = 0

    def __init__(self, name):
        self.team_name = name

    def add_win(self):
        self.team_games += 1
        self.team_wins += 1
        self.team_points += 3

    def add_tie(self):
        self.team_games += 1
        self.team_ties += 1
        self.team_points += 1

    def add_loss(self):
        self.team_games += 1
        self.team_losses += 1

    def __str__(self):
        return self.team_name + ": " + str(self.team_games) \
               + " " + str(self.team_wins) \
               + " " + str(self.team_ties) \
               + " " + str(self.team_losses) \
               + " " + str(self.team_points)


input_lst = [str(input()) for i in range(int(input()))]

lst = [i.split(";") for i in input_lst]

for elem in lst:
    elem[1] = int(elem[1])
    elem[3] = int(elem[3])

playersStats = {}
for elem in lst:
    if elem[0] not in playersStats:
        playersStats[elem[0]] = TeamStats(elem[0])
    if elem[2] not in playersStats:
        playersStats[elem[2]] = TeamStats(elem[2])

    if elem[1] > elem[3]:
        playersStats[elem[0]].add_win()
        playersStats[elem[2]].add_loss()
    elif elem[1] < elem[3]:
        playersStats[elem[0]].add_loss()
        playersStats[elem[2]].add_win()
    elif elem[1] == elem[3]:
        playersStats[elem[0]].add_tie()
        playersStats[elem[2]].add_tie()

for elem in playersStats.values():
    print(elem)