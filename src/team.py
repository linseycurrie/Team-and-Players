class Team:
    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach
        self.points = 0

    def add_player(self, player):
        self.players.append(player)

    def change_coach(self, new_coach):
        self.coach = new_coach

    def has_player(self, desired_player):
        for player in self.players:
            if player == desired_player:
                return True
        return False
        
    def points(self):
        return self.points

    def play_game(self, score):
        if score == True:
            self.points += 3

        

    

    