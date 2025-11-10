from rich.console import Console
from player_reader import PlayerReader
from player_stats import PlayerStats
from printing import Printer


console = Console()

def main():
    while True:
        season = console.input("Enter season [cyan](2018-19/2019-20/2020-21/2021-22/2022-23/2023-24/2024-25/2025-26)[/cyan] [magenta]blank to stop:[/magenta]")
        if season == "":
            break
        nationality = console.input("Enter nationality [cyan](USA/FIN/CAN/SWE/CZE/RUS/SLO/FRA/GBR/SVK/DEN/NED/AUT/BLR/GER/SUI/NOR/UZB/LAT/AUS)[/cyan] [magenta]blank to stop:[/magenta]")
        if nationality == "":
            break

        process_request(season, nationality)


def process_request(season: str, nationality: str) -> None:
    reader = PlayerReader(f"https://studies.cs.helsinki.fi/nhlstats/{season}/players")
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality(nationality)

    res = Printer(players, season, nationality)
    res.print_players()

if __name__ == "__main__":
    main()
