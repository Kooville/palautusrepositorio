

class PlayerStats:

    def __init__(self, reader):
        self.reader = reader
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        players_by_nation = [player for player in self.players if player.nationality == nationality]
        players_by_nation.sort(key=lambda p: p.points, reverse=True)
        return players_by_nation

    
        
