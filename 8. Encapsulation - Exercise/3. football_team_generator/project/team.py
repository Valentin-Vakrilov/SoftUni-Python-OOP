class Team:
    __players = []

    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating

    def add_player(self, player):
        if player not in self.__players:
            self.__players.append(player)
            return f"Player {player.name} joined team {self.__name}"

        return f"Player {player.name} has already joined"

    def remove_player(self, player_name):
        try:
            player = next(filter(lambda p: p.name == player_name, self.__players))
        except StopIteration:
            return f"Player {player_name} not found"

        self.__players.remove(player)
        return player


from player import Player


p = Player("Pall", 1, 3, 5, 7)

print("Player name:", p.name)
print("Points sprint:", p._Player__sprint)
print("Points dribble:", p._Player__dribble)
print("Points passing:", p._Player__passing)
print("Points shooting:", p._Player__shooting)

print("\ncalling the __str__ method")
print(p)

print("\nAbout the team")
t = Team("Best", 10)
print("Team name:", t._Team__name)
print("Teams points:", t._Team__rating)
print("Teams players:", len(t._Team__players))
print(t.add_player(p))
print(t.add_player(p))
print("Teams players:", len(t._Team__players))
print(t.remove_player("Pall"))
print(t.remove_player("Pall"))
