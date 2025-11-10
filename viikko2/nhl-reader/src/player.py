class Player:
    def __init__(self, dictionary):
        self.name = dictionary['name']
        self.nationality = dictionary['nationality']
        self.goals = dictionary['goals']
        self.team = dictionary['team']
        self.assists = dictionary['assists']

    @property
    def points(self):
        """Return total points (goals + assists)."""
        return self.goals + self.assists

    def __str__(self):
        return f"{self.name:20}  {self.team:15} {self.goals} + {self.assists} = {self.points}"
