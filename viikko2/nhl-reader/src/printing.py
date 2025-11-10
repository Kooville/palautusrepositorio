from rich.console import Console
from rich.table import Table

class Printer:
    def __init__(self, players, season, nationality):
        self.players = players
        self.season = season
        self.nationality = nationality

    def print_players(self):
        table = Table(title=f"Season {self.season} players from {self.nationality}")

        table.add_column("Name", justify="left", style="cyan", no_wrap=True)
        table.add_column("Teams", style="magenta")
        table.add_column("Goals", justify="right", style="green")
        table.add_column("Assists", justify="right", style="green")
        table.add_column("Points", justify="right", style="green")

        for player in self.players:
            table.add_row(
                player.name,
                player.team,
                str(player.goals),
                str(player.assists),
                str(player.points)
            )

        console = Console()
        console.print(table)
